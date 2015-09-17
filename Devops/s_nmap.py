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
    nm.scan(hosts=hosts,arguments=' -v -sS -p '+port)
except Exception,e:
    print 'Scan error:'+str(e)

for host in nm.all_hosts():
    print '-----------'
    print 'Host : %s (%s)' % (host,nm[host].hostname())
    print 'State : %s' % nm[host].state()
    for proto in nm[host].all_protocols():
        print '-----------'
        print 'Protocol : %s' % proto
        lport = nm[host][proto].keys()
        lport.sort()
        # print lport
        for port in lport:
            print 'port : %s\tstate : %s' % (port,nm[host][proto][port]['state'])