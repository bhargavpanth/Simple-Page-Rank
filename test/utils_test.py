import unittest
import re

class TestUtilities(unittest.TestCase):
	"""
	docstring for TestUtilities
	"""
	def __init__(self):
		self.url_regex = re.compile(
		r'^(?:http|ftp)s?://' # http:// or https://
		r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
		r'localhost|' #localhost...
		r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
		r'(?::\d+)?' # optional port
		r'(?:/?|[/?]\S+)$', re.IGNORECASE)

	def test_valid_url(self):
		'''
		returns if the URL is valid
		'''
		url = "http://test.com"
		match_status = re.match(self.url_regex, url) is not None
		self.assertEqual(True, match_status)

	# def test_status_code(self, content):
	# 	pass

	# def test_find_outgoing_urls(self):
	# 	pass

if __name__ == '__main__':
	unittest.main()
	
