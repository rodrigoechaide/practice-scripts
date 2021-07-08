#!/usr/bin/env python
#*-* coding: utf-8 *-*

from subprocess import Popen, PIPE
import os

command = "echo 1 > /proc/sys/net/ipv4/ip_forward"
command1= "echo hola > hola.txt"

p1 = Popen(command1.split(), stdout=PIPE, stderr=PIPE)
out, err = p1.communicate()


print out, err
