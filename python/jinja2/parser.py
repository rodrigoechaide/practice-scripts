import json
import os
import jinja2
from pprint import pprint
from jinja2 import Template

with open('template.json.jinja2') as f:
	template = Template(f.read())

data = {'registry_01': 'nexus.ascentio.com.ar:7443', 'registry_02': 'registry-dev.ascentio.com.ar', 'registry_03': 'registry-cms.ascentio.com.ar', 'registry_04': '192.168.233.229:5000', 'registry_05': '192.168.32.229:5000'}

output = template.render(data=data)

output_file = 'daemon.json'

with open(output_file, 'w') as f:
	f.write(output)
