#!/usr/bin/python
import re
import json


class Keyword:

	word_list = {}
	
	def __init__(self, args = {}):
		return
	
	def extract(self, data):
		content = self.remove_tags(data)
		content = self.trim(content)
		content = self.get_density(content)
		return content

	def remove_tags(self, data):
		# remove script
		removed = re.sub(r"<script[^<]*?>[\w\W\s\S]+?<\/script>", " ", data)
		
		# remove html special char
		removed = re.sub(r"&[\w\W]{4};", " ", removed)
		
		# remove ascii code
		removed = re.sub(r"\\x[\w]{2}", " ", removed)

		# remove html comment
		removed = re.sub(r"<!--[\W\w\S\s]+?-->", " ", removed)

		# remove style
		removed = re.sub(r"<style[^<]*?>[\w\W\s\S]+?<\/style>", " ", removed)

		# remove all tags
		removed = re.sub('<[^<]+?>', " ", removed)

		with open("./result/tags.txt", "w") as text_file:
			text_file.write(str(removed))

		return removed

	def trim(self, data):
		# remove newline
		removed = re.sub(r"(\\r|\\n|\\t|\s)+"," ", data)

		# remove non sentence component
		removed = re.sub(r"[^a-zA-Z0-9,\.]", " ", removed)

		# remove single char word
		removed = re.sub(r"\b\w\b", "", removed)

		# remove multiple whitespace
		removed = re.sub(r"\s+", " ", removed)

		with open("./result/tags-trim.txt", "w") as text_file:
			text_file.write(str(removed))

		return removed

	def get_density(self, data):

		# get single word density
		pattern = re.compile(r"[\W]+")

		data_single = pattern.split(data.lower())

		for word in data_single:
			if not word in self.word_list:
				self.word_list[word] = 1
			else:
				self.word_list[word] += 1

		
		# get two word density
		data_two = re.findall(r'(\w+\s\w+)', data)

		for word in data_two:
			if not word in self.word_list:
				self.word_list[word] = 1
			else:
				self.word_list[word] += 1


		with open("./result/words-list.txt", "w") as text_file:
			json.dump(self.word_list, text_file)


		return self.word_list


	def get_title(self):
		return "Keyword Density"

	def get_format(self):
		return ""

	def format(self, data):
		format = ""
		for key, value in data.items():
			format += "<tr><td>" + str(key) + "</td><td>" + str(value) + "</td></tr>"
			

		format = "<table class='table table-sm table-striped table-responsive'><thead><tr><th>Keyword</th><th>Density</th></tr></thead>" + "<tbody>" + format + "</ul>"+ "</tbody></table>"
		format = "<h2>" + self.get_title() + "</h2>" + format

		return format
