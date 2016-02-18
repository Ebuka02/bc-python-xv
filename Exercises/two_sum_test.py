import unittest
from two_sum import two_sum

class TwoSumTestSuite(unittest.TestCase):
	def test_list_range_8(self):
		res= two_sum([2,5,1,7], 8)
		self.assertEqual(res,[2,3])


	def test_list_range_15(self):
		res= two_sum([2,5,1,7,10,4], 15)
		self.assertEqual(res,[1,4])


	def test_list_range_6(self):
		res= two_sum([2,5,1,7,3], 6)
		self.assertEqual(res,[1,2])


	def test_list_range_14(self):
		res= two_sum([2,5,1,6,4,8], 14)
		self.assertEqual(res,[3,5])


	def test_list_range_7(self):
		res= two_sum([3,5,1,9,2], 7)
		self.assertEqual(res,[1,4])


	def test_list_range_10(self):
		res= two_sum([2,5,1,7,5], 10)
		self.assertEqual(res,[1,4])


	def test_list_range_12(self):
		res= two_sum([2,5,1,7], 12)
		self.assertEqual(res,[1,3])


	def test_list_range_16(self):
		res= two_sum([2,5,1,7,9], 16)
		self.assertEqual(res,[3,4])


	def test_list_range_11(self):
		res= two_sum([2,12,1,6,5,3], 11)
		self.assertEqual(res,[3,4])


	def test_list_range_21(self):
		res= two_sum([2,5,1,7,9,8,10,11], 21)
		self.assertEqual(res,[6,7])



if __name__ == '__main__' :
	unittest.main()