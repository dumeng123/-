
import unittest
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()
loader = unittest.defaultTestLoader
cases = loader.discover("E:\\python\\pythonProject1\\jisuqni",pattern="Test*.py")
suite.addTest(cases)
z = open("计算器方法.html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = z,
    title = "计算器方法报告",
    description = "这是一个计算器方法报告",
    verbosity = 1
)
runner.run(suite)