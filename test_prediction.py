'''
Tests Prediction class
'''
import unittest
from prediction import Prediction

from IPython import embed
from tournament import Tournament
from prediction_getter import WebPredictor


class DummyPredGetter(object):
    """Always returns 50:50"""

    def get_predictions(self, player1, player2, best_of):
        return Prediction({player1: .5, player2: .5})


class TestPrediction(unittest.TestCase):
    """Contaions prediction class tests"""

    def test_basic_intersect(self):
        prediction1 = Prediction({"p1": .5, "p2": .5})
        prediction2 = Prediction({"p3": .5, "p4": .5})
        intersect_pred = prediction1.intersect(prediction2, None,
                                                DummyPredGetter())
        self.assertEquals(sum(intersect_pred.values()), 1)
        self.assertTrue(all((val == .25 for val in intersect_pred.values())))


class TestTournament(unittest.TestCase):
    """Contains tournament class tests"""

    def test_json_loading(self):
        path = 'test_tournament.json'
        tournament = Tournament.from_json(path, WebPredictor())
        self.assertTrue(isinstance(tournament, Tournament))
        self.assertEquals(len(tournament.bracket), 3)

    def test_json_not_found(self):
        path = "lol_path.json"
        self.assertRaises(IOError, Tournament.from_json, path, WebPredictor())

    def test_prediction_calculation(self):
        path = 'test_tournament.json'
        tournament = Tournament.from_json(path, WebPredictor())
        final_prediction = tournament.calculate_prediction()
        self.assertEquals(len(final_prediction), 5)
        self.assertAlmostEquals(sum(final_prediction.values()), 1, 1)


if __name__ == "__main__":
    unittest.main()
