import unittest
import os


class RunCase(unittest.TestCase):
    def test_case01(self):
        casePath = os.path.join(os.getcwd(), 'case')
        suite = unittest.defaultTestLoader.discover(casePath, 'unittest_*.py')
        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    # unittest.main()
