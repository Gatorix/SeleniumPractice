import unittest


class FirstCase001(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('all_setup01')

    @classmethod
    def tearDownClass(cls) -> None:
        print('all_teardown01')

    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    # @unittest.SkipTest
    def testfirstcase(self):
        print(11)

    def testsecondcase(self):
        print(12)

    def testthirdcase(self):
        print(13)

    def testfourthcase(self):
        print(14)


if __name__ == "__main__":
    unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(FirstCase001('testsecondcase'))
    # unittest.TextTestRunner().run(suite)
