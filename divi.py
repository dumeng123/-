import unittest

from pythonProject1.cal import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [
    (9,3,3),
    (12,3,-4),
    (15,5,3)
]
@ddt
class TestCalcDivi(unittest.TestCase):

    @data(*data1)
    @unpack
    def testDivi(self,h,j,k):
        a = 4
        b = 2
        sum = 2
        c = Calc()
        s = c.divi(a,b)

        self.assertEqual(sum,s)