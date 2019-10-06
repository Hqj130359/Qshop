# assert 3>1,"第一个值不大于第二个值"
#
# assert 3>1,"第一值不大于第二个值"
#
# age=input(">>>>")
#
# assert age.isdigit(),"%s不是数字"%age
#
# int(age)

import unittest

class OurTest(unittest.TestCase):
    def setUp(self):
        """
        在测试执行之前自动执行，用于准备测试参数
        :return:
        """

        self.a=2
        self.b=2
    def test_equal(self):
        self.assertAlmostEquals(self.a,self.b) #断言是否相等

    def test_equall(self):
        self.assertNotAlmostEqual(self.a,self.b)