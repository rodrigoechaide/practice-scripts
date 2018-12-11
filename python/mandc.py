#!/usr/bin/env python
#*-* coding: utf-8 *-*

from lxml import etree
import os
import subprocess

def setup_mandc():
	'''Function to setup the monitor and control file'''
	root = etree.Element("executionStatus")
	etree.SubElement(root, "executionStartTime").text = subprocess.check_output("date +""%m""-%d-""%YT""%H:""%M:""%S.""%N", shell=True)
	etree.SubElement(root, "lastUpdateStatusFile").text = ""
	etree.SubElement(root, "unitID").text = "prueba"
	etree.SubElement(root, "apid").text = str(os.getpid())
	etree.SubElement(root, "Configfile").text = "/home/rodrigo/config.xml"
	etree.SubElement(root, "numbermaskips").text = "4"
	file = etree.ElementTree(root)
	file.write('statusfile.xml', pretty_print=True)
	print(etree.tostring(root, pretty_print=True))
	return root

def update_mandc(root):
	'''Function to update the monitor and control file'''
	for element in root.iter():
		if element.tag == "lastUpdateStatusFile":
			element.text = subprocess.check_output("date +""%m""-%d-""%YT""%H:""%M:""%S.""%N", shell=True)
	file = etree.ElementTree(root)
	file.write('statusfile.xml', pretty_print=True)
	print(etree.tostring(root, pretty_print=True))

root = setup_mandc()
update_mandc(root)
