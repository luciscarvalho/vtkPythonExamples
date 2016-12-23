import unittest

def f(x):
  return 2*x

class TestDoubling(unittest.TestCase):

    def test_integer(self):
        self.assertEqual(f(1), 2)
        self.assertEqual(f(3), 6)


if __name__ == '__main__':
    unittest.main()
