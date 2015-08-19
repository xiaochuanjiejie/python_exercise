__author__ = 'chuan'

import IPy

ip_s = raw_input('Print Ip or net-range: ')
ips  = IPy.IP(ip_s)
if len(ips) > 1:
    print 'Network is : %s:' % ips.net()
    print 'Netmask is: %s' % ips.netmask()
    print 'Broadcast is: %s' % ips.broadcast()
    print 'subnet is: %s' % ips.len(ips)
else:
    print 'reverse address: %s' % ips.reverseNames()[0]