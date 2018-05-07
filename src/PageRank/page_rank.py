import urllib
from bs4 import BeautifulSoup
import sys
# sys.path.append('./utils.py')
from utils import Utilities

class PageRank:

	"""
	PageRank - class to calulate set of page ranks given a seed URL
	"""
	
	def __init__(self, url):
		self.url = url

	# request for a URL parse contents from the response
	def get_document_content(self):
		print Utilities.parse_content("https://github.com")
		pass


	def calculate_outgoing_links(self, response):
		# parse the content with BS4
		pass


	def calculate_incoming_links(self):
		'''
		provide incoming link numbers to each of the websites
		'''

		pass

		