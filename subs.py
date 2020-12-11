import unittest

from pythonProject1.cal import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [
    (4,1,3),
    (-9,-1,-8),
    (9,8,1),
    (8,2,6)
]
@ddt
class TestCalcSubs(unittest.TestCase):
    @data(*data1)
    @unpack
    def testSubs(self, h, j, k):
        a = 4
        b = 2
        sum = 2
        c = Calc()
        s = c.subs(a, b)

        self.assertEqual(sum, s)