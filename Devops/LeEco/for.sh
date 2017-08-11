#!/bin/bash

echo -n "Input File_Name or Ip: "
read name
echo -n "Input Executable Statement: "
read exec1

if echo "$name" | grep -P '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'; then
  for ip in $name; do
    echo $ip
    sudo ssh $ip "$exec1"
  done
else
  for ip in $(cat $name); do
    echo $ip
    sudo ssh $ip "$exec1"
  done
fi
