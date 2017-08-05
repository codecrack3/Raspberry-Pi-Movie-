# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import re

class searchphim(object):
	def __init__(self, search):
		
		self.search = search;

	


	def get_result(self):
		try:
			html = requests.get('https://phim5s.herokuapp.com/search?q='+str(self.search)).text

			soup = BeautifulSoup(html,'lxml')
			result = soup.find_all("div",class_="child")
			
			return result
		except Exception, e:
			raise e


		
class stream_video(object):
	def __init__(self, url):
		super(stream_video, self).__init__()
		self.url = url
		
	def get_link(self):
		try:
			html = requests.get(self.url);
			soup = BeautifulSoup(html.text, "lxml")
			return soup.find('source')['src'].replace(';','&')
		except Exception, e:
			raise e

	