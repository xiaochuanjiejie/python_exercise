#!/bin/bash
set -x
#定义日期 目录 
Date=`date -d -1day +%Y%m%d`
Date_expire=`date -d -3day +%Y%m%d`
Cur_Date=`date '+%Y%m%d'`
log_dir="/letv/logs"
oldlog_dir="$log_dir/oldlogs"

#目录检测
if [ ! -d $oldlog_dir ]
    then
        mkdir -pv $oldlog_dir
        chown -R www.www $oldlog_dir
fi

#切割动作
if [ -d $log_dir -a $oldlog_dir ]
    then
        /usr/sbin/logrotate -f /etc/logrotate.d/ngxp
fi
sleep 5s
#移动文件
#for log_file in rsyncd.log hdcross.log php_errors.log php-fpm.log php-slow.log
path_list=(`ls -l /letv/logs/ngxp | awk '{print $NF}' | sed '1d'`)
for omit_path in php_errors.log php-slow.log; do
	if test "$omit_path" = "`echo ${path_list[*]}`"; then
		echo 'ok' > /dev/null
	else
		path_list=("${path_list[@]}" $omit_path)
	fi
done
for log_file in ${path_list[*]}
do
        per_dir=`echo $log_file|sed 's/\.log$//g'`
        [ -d $oldlog_dir/$per_dir ] || mkdir -pv $oldlog_dir/$per_dir
        [ -e $oldlog_dir/${log_file}-$Cur_Date ] && mv -v $oldlog_dir/${log_file}-$Cur_Date   $oldlog_dir/$per_dir/${log_file}-$Date   &&   echo 'log rotate done.'
        [ -e $oldlog_dir/$per_dir/${log_file}-$Date_expire ] && rm -rf $oldlog_dir/$per_dir/${log_file}-$Date_expire
done|logger -t rotate.sh
set +x
