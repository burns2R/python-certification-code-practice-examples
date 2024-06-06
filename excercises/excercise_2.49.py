import unittest

class TestString(unittest.TestCase):
    def test_string_contains(self):
        string = "Hello, world!"
        substring = "world"
        try:
            # Note: The code is looking to assert whether the substring is in string as true as seen in the expected output since the test ran correctly. Thus the right method is assertTrue
            # Proof: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue 
            self.assertTrue(substring in string)
        except AssertionError as e:
            print("error: ",e)
            raise

# Create TestSuite
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestString))

# Create a TextTestRunner with verbosity set to 2 for
# more detailed output.
runner = unittest.TextTestRunner(verbosity=3)

# Run the TestSuit and print the results
runner.run(suite)