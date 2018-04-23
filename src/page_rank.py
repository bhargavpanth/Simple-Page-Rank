import urllib
from bs4 import BeautifulSoup


class PageRank:

	"""docstring for PageRank"""
	
	def __init__(self, url):
		self.url = url


	def request(self):
		'''
		calculate the outgoing links from the current URL provided
		'''
		try:
			response = urllib.request(self.url)
		except Exception as e:
			raise
		else:
			if response.getcode() == 200:
				# pass the response to outgoing links
				self.calculate_outgoing_links(response)
			else:
				print 'web content was not retrieved'
				break
		finally: 
			pass


	def calculate_outgoing_links(self, response):
		# parse the content with BS4



	def calculate_incoming_links(self):
		'''
		provide incoming link numbers to each of the websites
		'''

		pass

		