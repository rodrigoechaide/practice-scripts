#!/usr/bin/env python
#*-* coding: utf-8 *-*

from lxml import etree
import os
import subprocess


NS = 'http://www.w3.org/2001/XMLSchema-instance'
location_attribute = '{%s}noNameSpaceSchemaLocation' % NS

root = etree.Element("executionStatus",attrib={'xmlnsxsi' : 'http://www.w3.org/2001/XMLSchema-instance', 'updateTime' : '1234'})
#root.set("interesting", "somewhat")

starttime = etree.SubElement(root, "executionStartTime")
starttime.text = str(os.system('date'))

lastupdate = etree.SubElement(root, "lastUpdateStatusFile")
lastupdate.text = subprocess.check_output("date +""%m""-%d-""%YT""%H:""%M:""%S", shell=True).strip()


unitID = etree.SubElement(root, "unitID")
unitID.text = "CHandler"

apid = etree.SubElement(root, "apid")
apid.text = str(os.getpid())

configfile = etree.SubElement(root, "Configfile")
configfile.text = "/home/rodrigo/config.xml"

numbermaskips = etree.SubElement(root, "numbermaskips")
numbermaskips.text = "4"

file = etree.ElementTree(root)
file.write('statusfile.xml', pretty_print=True)

print(etree.tostring(root, pretty_print=True))
