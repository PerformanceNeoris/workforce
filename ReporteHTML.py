import unittest
import HtmlTestRunner
#from HtmlTestRunner import HTMLTestRunner

class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertTrue(True)

class TestBar(unittest.TestCase):
    def test_bar(self):
        self.assertFalse(False)

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((
        loader.loadTestsFromTestCase(TestFoo),
        loader.loadTestsFromTestCase(TestBar)))
    outfile = file('Report.html', 'w')
    runner = HTMLTestRunner(stream=outfile,
                            verbosity=2,
                            title='LinkedIn Report',
                            description='This is a demo report')
    runner.run(suite)