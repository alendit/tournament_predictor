import unittest
from web_predictor import WebPredictor

from IPython import embed


class TestGetWebPredictions(unittest.TestCase):
    """Basic tests for getting web predictions"""

    def setUp(self):
        self.predictor = WebPredictor()
        self.player1 = "MC"
        self.player2 = "Vortix"
        self.player_non_unique = "HerO"
        self.best_of = 5

    def test_basic_getting(self):
        """Tests the chance of MC winning over Vortix"""

        site = self.predictor._get_page(self.player1,
                                        self.player2,
                                        self.best_of)
        self.assertIsNotNone(site)
        self.assertNotEqual(site.html(), "")

    def test_result_parsing(self):
        """Tests result page parsing"""
        site = self.predictor._get_page(self.player1,
                                        self.player2,
                                        self.best_of)

        result = self.predictor._parse_result(site)
        num_wins = self.best_of / 2 + 1
        self.assertEqual(len(result[0]), num_wins)
        self.assertEqual(len(result[1]), num_wins)
        self.assertAlmostEqual(sum(result[0]) + sum(result[1]), 100, 1)

    def test_result_getter(self):
        """Tests the public getter method."""
        prediction = self.predictor.get_predictions(self.player1,
                                                    self.player2, self.best_of)
        self.assertEqual(len(prediction), 2)
        self.assertTrue(self.player1 in prediction)
        self.assertTrue(self.player2 in prediction)
        self.assertAlmostEqual(sum(prediction.values()), 1, 2)

    def test_non_unique_nick(self):
        """Tests getting prediction for non-unique nicknames"""
        prediction = self.predictor.get_predictions(self.player1,
                                    self.player_non_unique, self.best_of)


if __name__ == "__main__":
    unittest.main()
