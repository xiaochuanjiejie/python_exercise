# -*- coding: UTF-8 -*-
__author__ = 'chuan'

import sys,nmap

scan_row = []
input_data = raw_input('Please input hosts and ports: ')
scan_row = input_data.split(" ")
if len(scan_row) != 2:
    print "Input error,example \"192.168.1.0/24 80,443,22\""
    sys.exit(0)
hosts = scan_row[0]
port  = scan_row[1]

try:
    #官方用例：http://xael.org/norman/python/python-nmap/
    nm = nmap.PortScanner()
except nmap.PortScannerError:
    print('Nmap not found',sys.exc_info()[0])
    sys.exit(0)

try:
    #’-sS‘代表TCP扫描，‘-sU’代表UDP扫描，参：https://nmap.org/man/zh/man-port-scanning-techniques.html
    nm.scan(hosts=hosts,arguments=' -v -sU -sS -p '+port)
except Exception,e:
    print 'Scan error:'+str(e)

for host in nm.all_hosts():
    print '-----------'
    print 'Host : %s (%s)' % (host,nm[host].hostname())
    print 'State : %s' % nm[host].state()
    print nm.command_line()
    print nm[host].all_protocols()
    for proto in nm[host].all_protocols():
        print '-----------'
        print 'Protocol : %s' % proto
        lport = nm[host][proto].keys()
        lport.sort()
        # print lport
        for port in lport:
            print 'port : %s\tstate : %s' % (port,nm[host][proto][port]['state'])
'''
既扫描给定port范围的tcp也扫描udp：
# python s_nmap.py
Please input hosts and ports: 123.57.154.241 22-125
-----------
Host : 123.57.154.241 ()
State : up
nmap -oX - -v -sU -sS -p 22-125 123.57.154.241
['tcp', 'udp']
-----------
Protocol : tcp
port : 22	state : open
port : 80	state : open
-----------
Protocol : udp
port : 123	state : open|filtered
'''