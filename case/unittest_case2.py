import unittest


class FirstCase002(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('all_setup02')

    @classmethod
    def tearDownClass(cls) -> None:
        print('all_teardown02')

    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    @unittest.SkipTest
    def testfirstcase2(self):
        print(21)

    def testsecondcase1(self):
        print(22)

    def testthirdcase3(self):
        print(23)

    def testfourthcase5(self):
        print(24)


if __name__ == "__main__":
    unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(FirstCase001('testsecondcase'))
    # unittest.TextTestRunner().run(suite)
