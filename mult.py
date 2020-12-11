import unittest

from pythonProject1.cal import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [
    (1,2,2),
    (-1,-1,1),
    (-9,-2,18)
]
@ddt
class TestCalcMult(unittest.TestCase):

    @data(*data1)
    @unpack
    def testMult(self,h,j,k):
        a = 2
        b = 2
        sum = 4
        c = Calc()
        s = c.mult(a,b)

        self.assertEqual(sum,s)