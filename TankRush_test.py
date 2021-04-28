import unittest
import TankRush


class TankRushTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(TankRush.TankRush(5,15,'000000000000000 000000000000000 000000100000000 000000000000000 000000000000000',3,5,'00000 00000 00001'), True)

    def test2(self):
        self.assertEqual(TankRush.TankRush(15,15,'900934352126360 119214144058652 979486082875698 322436531185165 887105930987956 232802644488782 302771989566798 073573207654780 311755785362806 909007939272309 395094805516080 562910805349811 993854324744973 768703404219199 630625270887199',2,2,'99 99'), True)

    def test3(self):
        self.assertEqual(TankRush.TankRush(3, 3, '321 694 798', 3, 2, '32 69 79'), True)

    def test4(self):
        self.assertEqual(TankRush.TankRush(7, 3, '727 158 735 425 235 123 432',
                                            6, 2, '72 15 73 42 23 12'), True)

    def test5(self):
        self.assertEqual(TankRush.TankRush(3, 4, "1234 2345 0987", 2, 2, "23 98"), False)

    def test6(self):
        self.assertEqual(TankRush.TankRush(3, 8, '7277604 1583078 1427735', 3, 2, '78 35 20'), False)

    def test7(self):
        self.assertEqual(TankRush.TankRush(3, 15, '993854324744973 768703404219199 630625270887199',
                                            2, 2, '99 99'), True)

if __name__ == '__main__':
    unittest.main()