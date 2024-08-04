import unittest

from src.score import Score
from src.model import Word

class TestScore(unittest.TestCase):

    def test_getWordScore(self):
        word = Word('test', 1, 0, False)
        # word start        10
        # not word end       0
        # not leaf           0
        # depth 1            1
        # match length 3     3
        # multiplier         3
        # total             14*3 = 42
        self.assertEqual(Score.getWordScore(word, 0, 'tes'), 42)
        # not word start    0
        # word end          5
        # not leaf          0
        # depth 1           1
        # match length 2    2
        # multiplier        2
        # total             8 * 2 = 16
        self.assertEqual(Score.getWordScore(word, 2, 'st'), 16)
        word.isLeaf = True
        word.depth = 3
        # word start        10
        # word end           5
        # is leaf           10
        # depth 3            3
        # match length 4     4
        # multiplier         4
        # total             32 * 4 = 128
        self.assertEqual(Score.getWordScore(word, 0, 'test'), 128)

    def test_adjustForUnusedChars(self):
        self.assertEqual(Score.adjustForUnusedChars(100, 0), 100)
        self.assertEqual(Score.adjustForUnusedChars(100, 1), 90)
        self.assertEqual(Score.adjustForUnusedChars(99, 1), 89)
        self.assertEqual(Score.adjustForUnusedChars(101, 1), 90)
        self.assertEqual(Score.adjustForUnusedChars(100, 2), 81)