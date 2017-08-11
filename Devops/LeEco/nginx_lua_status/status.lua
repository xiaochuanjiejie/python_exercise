local cjson = require("cjson")
local dict = ngx.shared.host_dict
local statsDict = ngx.shared.stats_dict
fs="|"
ofs="||"

defaultFormat="json"
statsList={ 
	"inbytes",
	"outbytes",
	"small499",
	"big499",
	"maxconn502",
	"normal502",
	"uprt500.count",
	"ngxrt1s.count",
	"GET",
}

reqsList = { "reqs" }

rtList = {
	"upstream.time",
	"request.time",
	"nginx.time"
}

local function execString(name)
	param="ngx.var."..name
	local script = "return "..param
	return loadstring(script)()
end

local function updateStats(host,key,value)
    mkey=fs.."stats"..fs..host..fs..key
    newvalue = statsDict:set(mkey, value)
    return newvalue
end

local function getLastStats()
	lastStats={}
	for host in string.gmatch((dict:get("hosts") or ""), "[^,|]+") do
        if  lastStats[host] == nil then
            lastStats[host] = {}
        end
        for k,v in pairs(rtList) do
			key=fs.."stats"..fs..host..fs..v
			lastStats[host][v]= statsDict:get(key) or 0
    	end 
        for k,v in pairs(reqsList) do
			key=fs.."stats"..fs..host..fs..v
			lastStats[host][v]= statsDict:get(key) or 0
    	end 
	end
	lastStats["timestramp"]=statsDict:get("timestramp")
	local data1=cjson.encode(lastStats)
	return data1
end

local function systemStatus()
	outData2={}
	outData2["system"]={}
    varList={"host", "hostname","nginx_version","server_name","server_addr","server_port"}
    varList={"connections_active","connections_reading","connections_waiting","connections_writing"}
	for i=1,#varList do   
		outData2["system"][varList[i]]=execString(varList[i])
	end
	if (ngx.var.nginx_version >= '1.8.0') then
		outData2["system"]["ngx.worker.count"]=ngx.worker.count()
		outData2["system"]["run.count"]=ngx.timer.running_count()
		outData2["system"]["ngx.timer.pending.count"]=ngx.timer.pending_count()
	end
	outData2["system"]["ngx.status"]=ngx.status
	outData2["system"]["pid"]=ngx.var.pid
	--outData2["system"]["nginx_configure"]=ngx.config.nginx_configure()
	--outData2["system"]["ngx_lua_version"]=ngx.config.ngx_lua_version
	--outData2["system"]["ngx-localtime1"]=ngx.localtime()
	--outData2["system"]["ngx-utctime"]=ngx.utctime()
	--outData2["system"]["ngx-time"]=ngx.time()
	--outData2["system"]["ngx-update_time"]=ngx.update_time()
	--outData2["system"]["ningx_version"]=ngx.config.nginx_version
	--outData2["system"]["ngx-now"]=ngx.now()
	local data3=cjson.encode(outData2)
	return data3
	--ngx.say(data3)
end

local function outJson() 
	outData={}
	lastData={}
	tData={}
	for host in string.gmatch((dict:get("hosts") or ""), "[^,|]+") do
        if outData[host] == nil then
            outData[host]={}
        end

        if lastData[host] == nil then
            lastData[host]={}
        end

        if tData[host] == nil then
            tData[host]={}
        end

        for i = 100, 600, 1 do
			key=fs.."hosts"..fs..host..fs.."http"..i
            local count1 = dict:get(key)
            if count1 then
                outData[host]["http"..i]=count1
            end
        end

		lastData=cjson.decode(getLastStats())
		-- get current data
        for k,v in pairs(statsList) do
			key=fs.."hosts"..fs..host..fs..v
            local count6 = dict:get(key)
            if count6 then
            	outData[host][v] = count6
        	end
    	end 
		statsDict:set("timestramp",os.time())

		-- update data
        for k,v in pairs(reqsList) do
			key = fs.."hosts"..fs..host..fs..v
            local count6 = dict:get(key)
        	if count6 then
				updateStats(host,v,count6 or 0)
            	outData[host][v]=count6
        	end

		end

        for k,v in pairs(rtList) do
			reqsKey=fs.."hosts"..fs..host..fs..'reqs'
			key = fs.."hosts"..fs..host..fs..v
			skey = fs.."stats"..fs..host..fs..v
            local count6 = dict:get(key)
        	if count6 then
				updateStats(host,v,count6 or 0)
            	--outData[host][v]=count6
        	end
			rtChange = count6 - lastData[host][v] 
			
			--ngx.say(v.."|"..count6.."|"..lastData[host][v].."|"..rtChange.."<br>")
			reqsChange = outData[host]["reqs"] - (lastData[host]["reqs"] or 0 ) 
			
			if not reqsChange or reqsChange == 0  then 
				reqsChange = 1
			end
			avgData=string.format("%.2f",rtChange / (reqsChange or 1)*1000)+0
			
			if avgData < 0 then
				avgData = 0
			end
			outData[host][v..".avg"] = avgData 
    	end 
		
	end

    systemOut=cjson.decode(systemStatus())
	outData["system"]={}
	for k,v in pairs(systemOut["system"]) do
		outData["system"][k]=v
	end
    ngx.say(cjson.encode(outData))
end

format = ngx.req.get_uri_args()["format"] or defaultFormat

if format == "json" then
    outJson()
end

if ngx.req.get_uri_args()["clear"] == "1"  then
    dict:flush_all()
    statsDict:flush_all()
end
