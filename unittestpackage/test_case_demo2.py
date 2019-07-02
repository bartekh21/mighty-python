import unittest


class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("#" * 30)
        print("I will run only once before all tests")
        print("#" * 30 + "\n")

    def setUp(self):
        print("I will run once before every test")

    def test_methodA2(self):
        print("Running method A")

    def test_methodB2(self):
        print("Running method B")

    def tearDown(self):
        print("I will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("#" * 30)
        print("I will run only once after all tests")
        print("#" * 30 + "\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
