#!/usr/bin/python


class MetaData:
	
	def __init__(self, args = {}):
		return
	
	def extract(self, data):
		import re
		import json
		matches = re.findall('(<meta[^\/]+?\/>)', data)
		return matches

	def get_title(self):
		return "Meta Data"

	def get_format(self):
		return ""