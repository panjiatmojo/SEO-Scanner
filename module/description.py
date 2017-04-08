#!/usr/bin/python


class Description:
	
	def __init__(self, args = {}):
		return
	
	def extract(self, data):
		import re
		import json
		matches = re.findall('(<meta[^<]*?name=(\"|\')description(\"|\')[^<]*?>)', data)
		matches = re.findall('content=("|\')(.+?)("|\')', matches[0][0])

		return matches[0][1]

	def get_title(self):
		return "Description"

	def get_format(self):
		return ""

	def format(self, data):
		import html
		format = ""
		format += html.escape(data) 

		format = "<h2>" + self.get_title() + "</h2>" + format

		return format