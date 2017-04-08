#!/usr/bin/python
import re


class Keyword:
	
	def __init__(self, args = {}):
		return
	
	def extract(self, data):
		content = self.remove_tags(data)
		content = self.trim(content)
		return content

	def remove_tags(self, data):
		# remove all tags
		removed = re.sub(r"<script[^<]*?>[\w\W\s\S]+?<\/script>", " ", data)
		removed = re.sub(r"&[\w\W]{4};", " ", removed)
		removed = re.sub(r"\\x[\w]{2}", " ", removed)
		removed = re.sub(r"<!--[\W\w\S\s]+?-->", " ", removed)
		removed = re.sub(r"<style[^<]*?>[\w\W\s\S]+?<\/style>", " ", removed)
		removed = re.sub('<[^<]+?>', " ", removed)

		with open("./result/tags.txt", "w") as text_file:
			text_file.write(str(removed))

		return removed

	def remove_style(self, data):
		removed = re.sub(r"<style[^<]>[\w\W\s\S]+?<\/style>", " ", data)
		return removed


	def trim(self, data):
		
		removed = re.sub(r"(\\r|\\n|\\t|\s)+"," ", data)
		removed = re.sub(r"[^a-zA-Z0-9,\.]", " ", removed)

		removed = re.sub(r"\s+", " ", removed)

		with open("./result/tags-trim.txt", "w") as text_file:
			text_file.write(str(removed))

		return removed



	def get_title(self):
		return "Keyword"

	def get_format(self):
		return ""