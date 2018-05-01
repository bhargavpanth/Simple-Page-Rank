
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
			response = urllib.urlopen(url.encode('utf-8'))
		except Exception as e:
			raise
		else:
			if response.getcode() == 200:
				return response
			else:
				print 'web content was not retrieved'
				pass
		finally:
			pass

"""
def main():
	test = Utilities()
	resp = test.parse_content('http://github.com')
	print resp

if __name__ == '__main__':
	main()
"""
	