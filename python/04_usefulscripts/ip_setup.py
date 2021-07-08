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



IPs = {'GW':'10.0.1.1', 'Mask':'255.0.0.0'}
command = ("ifconfig eth0:1 %(GW)s netmask %(Mask)s" %IPs,)

out, err = run_command(command)

print len(out)
print len(err)
