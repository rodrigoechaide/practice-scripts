#!/usr/bin/env python
#*-* coding: utf-8 *-*

from lxml import etree
import StringIO
from datetime import datetime

def parse_connections(path):

    """
    Iterates over the <connections> xml node.
    Returns a list of dicts, having each one an IPreal, IPmask pair.

    i.e.:
    maskList = [{'IPreal':'190.216.68.163', 'IPmask':'192.168.0.253'},
                {'IPreal':'190.216.68.164', 'IPmask':'192.168.0.254'},]
    """
    maskList = []
    connectionsNode = tree.find(path)

    for mask in connectionsNode:
        maskDict = {}
        maskDict["IPreal"] = mask.find('IPreal').text
        maskDict["IPmask"] = mask.find('IPmask').text
        maskList.append(maskDict)

    return maskList


f = open("config.xml", 'r')
xml_string = f.read()

print xml_string

xmlparser = etree.XMLParser(remove_comments=True,
                            remove_blank_text=True)

config_vars = {}

tree= etree.fromstring(xml_string, xmlparser)

config_vars['unitID']=tree.find('unitID').text
log = tree.find('log')
config_vars['logEnable'] = True if log.get('enable') == 'true' else False
config_vars['logFileName'] = (log.find('logFileName').text).replace('@date', datetime.now().strftime("%Y%m%d"))
config_vars['logDirectory'] = log.find('logDirectory').text
config_vars['logLevel'] = log.find('logLevel').text
fm =tree.find('fileMonitor')
config_vars['monitorEnable']= True if fm.get('enable') == 'true' else False
config_vars['monitorDirectory'] = fm.find('monitorDirectory').text
config_vars['monitorFileName'] = (fm.find('monitorFileName').text).replace('@date', datetime.now().strftime("%Y%m%d"))
config_vars['maskList'] = parse_connections('connections')

print config_vars['logFileName']

print config_vars
