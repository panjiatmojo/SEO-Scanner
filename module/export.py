#!/usr/bin/python
import re
import json
import os 

class Export:

	content = ""

	def __construct__():
		return

	def generate(self):
		dir_path = os.path.dirname(os.path.realpath(__file__))

		with open(dir_path + "/template/template.html") as f:
			template = f.read()

		document = re.sub(r"\{\{title\}\}", self.title, template)
		document = re.sub(r"\{\{content\}\}", self.content, document)

		with open("./result/result.html", "w") as text_file:
			text_file.write(str(document))

		return document	

	def get_header():
		return

	def set_title(self, data):
		self.title = data

	def add_content(self,data):
		self.content += data
		return True


