'''
Tests Prediction class
'''
import unittest
from prediction import Prediction

from IPython import embed


class DummyPredGetter(object):
    """Always returns 50:50"""

    def get_predictions(self, player1, player2, best_of):
        return Prediction({player1: .5, player2: .5})


class TestPrediction(unittest.TestCase):
    """Contaions prediction class tests"""

    def testBasicIntersect(self):
        prediction1 = Prediction({"p1": .5, "p2": .5})
        prediction2 = Prediction({"p3": .5, "p4": .5})
        intersect_pred = prediction1.intersect(prediction2, None,
                                                DummyPredGetter())
        self.assertEquals(sum(intersect_pred.values()), 1)
        self.assertTrue(all((val == .25 for val in intersect_pred.values())))


if __name__ == "__main__":
    unittest.main()
