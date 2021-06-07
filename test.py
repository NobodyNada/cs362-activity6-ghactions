import unittest
import calc


class CalcTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(-1, 3), 2)
        self.assertEqual(calc.add(5, 0), 5)
        self.assertAlmostEqual(calc.add(0.1, 0.2), 0.3)

    def test_sub(self):
        self.assertEqual(calc.sub(3, 2), 1)
        self.assertEqual(calc.sub(2, 3), -1)
        self.assertAlmostEqual(calc.sub(5.5, 0.5), 5)

    def test_mul(self):
        self.assertEqual(calc.mul(3, 4), 12)
        self.assertEqual(calc.mul(2, 0), 0)
        self.assertEqual(calc.mul(-1, -1), 1)

    def test_div(self):
        self.assertAlmostEqual(calc.div(3, 4), 0.75)
        self.assertEqual(calc.div(4, -2), -2)

if __name__ == '__main__':
    unittest.main()
