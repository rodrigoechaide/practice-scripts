#!/usr/bin/env python3
# *-* coding:utf-8 *-*

import re

str = "The rain in Spain falls mainly in the plain!"

print("Check if the string: {} contains \"ai\" followed by 0 or more \"x\" characters:".format(str) )

x = re.findall("aix*", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

