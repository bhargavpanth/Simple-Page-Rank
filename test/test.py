import sys
sys.path.append('../src')
from page_rank import PageRank
import unittest


class TestPageRankSanity(unittest.TestCase):

	def test_objectCreation(self):
		test = PageRank('http://github.com/')
		self.assertTrue(type(test) is instance)


if __name__ == '__main__':
	unittest.main()
	
