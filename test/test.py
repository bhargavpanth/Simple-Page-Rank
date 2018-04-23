import sys
sys.path.append('../src')
from page_rank import PageRank
import unittest

class TestPageRankSanity(unittest.TestCase):

	def test_object_creation(self):
		test = PageRank('http://github.com/')
		print type(test)


if __name__ == '__main__':
	unittest.main()
	
