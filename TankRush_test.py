import unittest
import TankRush


class TankRushTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(TankRush.TankRush(5,15,'000000000000000 000000000000000 000000100000000 000000000000000 000000000000000',3,5,'00000 00000 00001'), True)

if __name__ == '__main__':
    unittest.main()