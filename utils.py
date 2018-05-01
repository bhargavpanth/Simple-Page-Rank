
from bs4 import BeautifulSoup
import urllib

class Utilities:
	"""
	Generic class for utilities
	* URL request
	* Content parsing using BS4
	"""

	def __init__(self):
		pass

	def parse_content(self, url):
		# ensure url is utf-8 encoded
		try:
			content = urllib.request(url.encode('utf-8'))
		except Exception as e:
			raise
		else:
			if response.getcode() == 200:
				# pass the response to outgoing links
				return response
			else:
				print 'web content was not retrieved'
				break
		finally: 
			pass

	def function():
		pass