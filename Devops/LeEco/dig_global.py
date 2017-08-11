#!/usr/bin/python
#-*- coding: utf-8 -*-
###########################
#HK DNS:
#202.45.84.58	203.80.96.10
#TW DNS:
#211.78.215.137	211.78.215.200
#USA DNS:
#8.8.8.8	206.214.214.28
#电信：
#101.226.4.6	218.30.118.6
#联通
#123.125.81.6	140.207.198.6
###########################

from subprocess import PIPE, Popen
import re

dns_hk = ['202.45.84.58','203.80.96.10']
dns_usa = ['206.214.214.28','184.169.139.227','50.22.147.234','8.8.8.8']
dns_ct = ['219.150.32.132','218.30.118.6']
dns_cnc = ['202.106.0.20','123.125.81.6','140.207.198.6']
dns_bgp = ['211.167.230.100','211.167.230.200']

url = raw_input('Input url(eg: a.com,b.com): ')
list_url = url.split(",")
patt = '\d+.\d+.\d+.\d+'

for read_url in list_url:
	p = Popen('dig +nocmd +nocomment +nostat %s @%s' % (read_url,dns_hk[0]), shell=True, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate()
	print '香港解析: %s' % stdout
	if re.search(patt,stdout) is None:
		p = Popen('dig +nocmd +nocomment +nostat %s @%s' % (read_url,dns_hk[1]), shell=True, stdout=PIPE, stderr=PIPE)
		stdout, stderr = p.communicate()
		print '香港解析: %s' % stdout
	p = Popen('dig +nocmd +nocomment +nostat %s @%s' % (read_url,dns_usa[0]), shell=True, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate()
	print '北美解析: %s' % stdout
	if re.search(patt,stdout) is None:
		p = Popen('dig +nocmd +nocomment +nostat %s @%s' % (read_url,dns_usa[1]), shell=True, stdout=PIPE, stderr=PIPE)
		stdout, stderr = p.communicate()
		print '北美解析: %s' % stdout
	print dns_ct[0]
	p = Popen('dig +nocmd +nocomment +nostat %s @%s' % (read_url,dns_ct[0]), shell=True, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate()
	print '电信解析: %s' % stdout
	if re.search(patt,stdout) is None:
		p = Popen('dig +nocmd +nocomment +nostat %s @%s' % (read_url,dns_ct[1]), shell=True, stdout=PIPE, stderr=PIPE)
		stdout, stderr = p.communicate()
		print '电信解析: %s' % stdout
	print dns_cnc[0]
	p = Popen('dig +nocmd +nocomment +nostat %s @%s' % (read_url,dns_cnc[0]), shell=True, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate()
	print '联通解析: %s' % stdout
	if re.search(patt,stdout) is None:
		p = Popen('dig +nocmd +nocomment +nostat %s @%s' % (read_url,dns_cnc[1]), shell=True, stdout=PIPE, stderr=PIPE)
		stdout, stderr = p.communicate()
		print '联通解析: %s' % stdout
	print dns_bgp[0]
	p = Popen('dig +nocmd +nocomment +nostat %s @%s' % (read_url,dns_bgp[0]), shell=True, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate()
	print 'BGP解析: %s' % stdout
	if re.search(patt,stdout) is None:
		p = Popen('dig +nocmd +nocomment +nostat %s @%s' % (read_url,dns_bgp[1]), shell=True, stdout=PIPE, stderr=PIPE)
		stdout, stderr = p.communicate()
		print 'BGP解析: %s' % stdout
	print "**********************"
