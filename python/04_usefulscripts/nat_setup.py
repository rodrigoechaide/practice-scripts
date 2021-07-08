#!/usr/bin/env python
#*-* coding: utf-8 *-*

from subprocess import Popen, PIPE

def run_command(command):
    """
    Method for running commands and getting its outputs and errors.
    """
    out_list = []
    err_list = []
    c = 0	
    for i in command:
    	p1 = Popen(i.split(), stdout=PIPE, stderr=PIPE)
    	out, err = p1.communicate()
    	# Quitamos los enters de más al final:
    	out_list.append(out.strip())
	err_list.append(err.strip())
    	print "Executing command: %s" % i
	if out_list[c]!="":
    	    print "Command output: %s" % out_list[c]
	if err_list[c]!="":
	    print "Command error: %s" % err_list[c]	
	c = c + 1
    return out_list, err_list



mask = {'IPreal':'190.216.68.163', 'IPmask':'192.168.0.253'}
command = ("iptables -t nat -A PREROUTING -d %(IPmask)s -j DNAT --to %(IPreal)s" % mask, "iptables -t nat -A POSTROUTING -s %(IPreal)s -j SNAT --to %(IPmask)s" % mask)

out, err = run_command(command)

print len(out)
print len(err)
