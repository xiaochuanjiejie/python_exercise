#!/bin/bash


program=/usr/local/LeMonitor/scripts/nginxMon/bin/nginxMon.py
logDir=/letv/logs/LeMonitor/scripts/nginxMon/
[ ! -d $logDir ] && mkdir -p ${logDir}

python ${program}  1>>${logDir}/app.log 2>&1 
