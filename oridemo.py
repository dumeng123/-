import unittest

from pythonProject1.cal import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [
    (1,2,3),
    (-9,-1,-10),
    (-9,8,-1)
]
@ddt
class TestCalcAdd(unittest.TestCase):

    @data(*data1)
    @unpack
    def testAdd(self,h,j,k):
        a = 2
        b = 2
        sum = 4
        c = Calc()
        s = c.add(a,b)

        self.assertEqual(sum,s)





