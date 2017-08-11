#!/bin/bash

echo -n "Input File_Name or Ip: "
read name
declare -a total
echo -n "Input File & Path(filename /tmp/tmp): "
read -ra total

if echo "$name" | grep -P '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'; then
  for ip in $name; do
    echo $ip
    sudo scp ${total[0]} root@$ip:${total[1]}
  done
else
  for ip in $(cat $name); do
    echo $ip
    sudo scp ${total[0]} root@$ip:${total[1]}
  done
fi
