import unittest
from unittestpackage.test_case_demo1 import TestCaseDemo1
from unittestpackage.test_case_demo2 import TestCaseDemo2

# get tests from classes TestCaseDemo1 and TestCaseDemo2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)

# create a Test Suite combining both classes

smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)


