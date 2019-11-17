#coding:utf-8
import unittest
class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('类执行之前的方法')
    @classmethod
    def tearDownClass(cls):
        print('类执行之后的方法')
    def test_01(self):
        print('测试方法1')
    def test_02(self):
        print('测试方法2')
if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
