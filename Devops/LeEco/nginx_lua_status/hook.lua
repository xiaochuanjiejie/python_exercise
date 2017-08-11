
local fs='|'
local function incr(host,key,value)
    mkey=fs.."hosts"..fs..host..fs..key
    tkey=fs.."hosts"..fs.."total"..fs..key
    local host_dict = ngx.shared.host_dict
    value = value or 1
    local newvalue, err = host_dict:incr(mkey, value)
    if err then
        host_dict:set(mkey, value)
        newvalue = value
    end
    local newvalue1, err1 = host_dict:incr(tkey, value)
    if err1 then
        host_dict:set(tkey, value)
        newvalue = value
    end
    return newvalue
end


local host = ngx.var.host

if incr("total","|count") == 1 then
    local host_dict = ngx.shared.host_dict
    host_dict:set("hosts", (host_dict:get("hosts") or "")..fs.."total")
end
if incr(host,"|count") == 1 then
    local host_dict = ngx.shared.host_dict
    host_dict:set("hosts", (host_dict:get("hosts") or "")..fs..host)
end

incr(host,"inbytes",ngx.var.request_length + 0)
incr(host,"outbytes",ngx.var.bytes_sent + 0)
incr(host,"http"..ngx.var.status)
incr(host,"reqs")
incr(host,ngx.req.get_method())

local upstream_time = tonumber(ngx.var.upstream_response_time) or 0
local request_time = tonumber(ngx.var.request_time) or 0
local ngxtime = request_time - upstream_time

incr(host,"upstream.time",upstream_time)
incr(host,"request.time",request_time)
incr(host,"nginx.time",ngxtime)

if upstream_time >= 0.5 and ngx.var.status ~= "504" then
    incr(host,"uprt500.count")
end

if ngxtime >= 1 and ngx.var.status ~= "504" then
    incr(host,"ngxrt1s.count")
end

local status2 = tonumber(ngx.var.status)

if request_time >=0.5 and status2 == 499 then
    incr(host,"big499")
elseif request_time <0.5 and status2 == 499 then
    incr(host,"small499")
end

if upstream_time == 0 and status2 == 502 then
    incr(host,"maxconn502")
elseif upstream_time ~= 0 and status2 == 502 then
    incr(host,"normal502")
end

if status2 <400 then
    incr(host,"2xx")
elseif status2 >=400 then
    incr(host,"4xx")
    incr(host,"error.count")
elseif status2 >=500 then
    incr(host,"5xx")
    incr(host,"error.count")
end
