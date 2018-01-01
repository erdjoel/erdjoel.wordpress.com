"""
Tests built for unittest are classes extending unittest.TestCase.

By convention, methods starting with *test_* are recognized as test to be run

setUp() and tearDown() are automatically executed once before and after all test.
You can share references between setUp, tearDown and test_* methods via self

"""

import random
import unittest


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


if __name__ == '__main__':
    unittest.main()  # not really necessary if you use python -m unittest.


"""
assertion methods (http://docs.python.org/2/library/unittest.html):
- assert: base assert allowing you to write your own assertions
- assertEqual(a, b): check a and b are equal
- assertNotEqual(a, b): check a and b are not equal
- assertIn(a, b): check that a is in the item b
- assertNotIn(a, b): check that a is not in the item b
- assertFalse(a): check that the value of a is False
- assertTrue(a): check the value of a is True
- assertIsInstance(a, TYPE): check that a is of type "TYPE"
- assertRaises(ERROR, a, args): check that when a is called with args that it raises ERROR
"""

"""
test cases file should start with the test* prefix (like test_tennis.py), so that they can be found automatically:

> python -m unittest discover

Thus file filtering can be applied to run only a file (tests for a module), only a class, or only a test method:

> python -m unittest test_learning
> python -m unittest test_learning.TestSequenceFunctions
> python -m unittest test_learning.TestSequenceFunctions.test_shuffle
"""

"""
test winning condition of tennis game

class TestSetWinning(TestCase):
    def test_score_grows(self):
        set = Set()
        self.assertEqual("0", set.firstScore())
        set.firstScores()  # first player make a score
        self.assertEqual("15", set.firstScore())
        self.assertEqual("0", set.secondScore())
        set.secondScores()  # second player make a score
        self.assertEqual("15", set.secondScore())
        
    def test_player_1_win_when_scores_at_40(self):
        set = Set()
        set.firstScores(3)
        self.assertEqual(None, set.winner())
        set.firstScores()
        self.assertEqual(1, set.winner())
        
    def test_player_2_win_when_scores_at_40(self):
        set = Set()
        set.secondScores(3)
        self.assertEqual(None, set.winner())
        set.secondScores()
        self.assertEqual(2, set.winner())
        
    def test_deuce_requires_1_more_than_one_ball_to_win(self):
        set = Set()
        set.firstScores(3)
        set.secondScores(3)
        set.firstScores()
        self.assertEqual(None, set.winner())
        set.firstScores()
        self.assertEqual(1, set.winner())
        
    def test_deuce_requires_2_more_than_one_ball_to_win(self):
        set = Set()
        set.firstScores(3)
        set.secondScores(3)
        set.secondScores()
        self.assertEqual(None, set.winner())
        set.secondScores()
        self.assertEqual(2, set.winner())
        
    def test_player_can_return_to_deuce_by_scoring_against_the_others_advantage(self):
        set = Set()
        set.firstScores(3)
        set.secondScores(3)
        self.assertEqual(None, set.winner())
        set.firstScores()
        set.secondScores()
        set.firstScores()
        set.secondScores()
        self.assertEqual(None, set.winner())
        self.assertEqual("40", set.firstScore())
        self.assertEqual("40", set.secondScore())
        
class TestScoreNames(TestCase):
    def test_score_names(self):
        scores = Scores()
        self.assertEqual("0", scores.scoreName(0))
        self.assertEqual("15", scores.scoreName(1))
        self.assertEqual("30", scores.scoreName(2))
        self.assertEqual("40", scores.scoreName(3))
        self.assertEqual("A", scores.scoreName(4))
"""