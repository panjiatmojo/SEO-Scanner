#!/usr/bin/python


class Title:
	
	def __init__(self, args = {}):
		return
	
	def extract(self, data):
		import re
		import json
		matches = re.findall('<title[^<]*?>(.+?)<\/title>', data)
		return matches

	def get_title(self):
		return "Title"

	def get_format(self):
		return ""

	def format(self, data):
		import html
		format = ""
		for datum in data:
			format += "<li>" + html.unescape(datum) + "</li>"

		format = "<ul>" + format + "</ul>"
		format = "<h2>" + self.get_title() + "</h2>" + format

		return format