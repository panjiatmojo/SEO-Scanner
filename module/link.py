#!/usr/bin/python


class Link:
	
	def __init__(self, args = {}):
		return
	
	def extract(self, data):
		import re
		matches = re.findall(r"<link[^<].+?>", data)
		return matches

	def get_title(self):
		return "Links"

	def get_format(self):
		return ""

	def format(self, data):
		import html
		format = ""
		for datum in data:
			format += "<li>" + html.escape(datum) + "</li>"

		format = "<ul>" + format + "</ul>"
		format = "<h2>" + self.get_title() + "</h2>" + format

		return format