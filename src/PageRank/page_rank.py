import urllib
from bs4 import BeautifulSoup
import sys
sys.path.append('../../utils')
from utils import Utilities

class PageRank:

	"""docstring for PageRank"""
	
	def __init__(self, url):
		self.url = url

	# request for a URL parse contents from the response
	def get_document_content(self):
		Utilities.parse_content("https://github.com")
		pass


	def calculate_outgoing_links(self, response):
		# parse the content with BS4
		pass


	def calculate_incoming_links(self):
		'''
		provide incoming link numbers to each of the websites
		'''

		pass

		