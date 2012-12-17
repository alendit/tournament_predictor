import unittest
from prediction_getter import WebPredictor

from IPython import embed

class TestGetWebPredictions(unittest.TestCase):
    """Basic tests for getting web predictions"""

    def setUp(self):
        self.predictor = WebPredictor()
        self.player1 = "MC"
        self.player2 = "Vortix"
        self.best_of = 5

    def test_basic_getting(self):
        """Tests the chance of MC winning over Vortix"""


        site = self.predictor._get_page(self.player1,
                                        self.player2,
                                        self.best_of)
        self.assertIsNotNone(site)
        self.assertEqual(site.getcode(), 200)
        self.assertNotEqual(site.read(), "")

    def test_result_parsing(self):
        """Tests result page parsing"""
        site = self.predictor._get_page(self.player1,
                                        self.player2,
                                        self.best_of)

        result = self.predictor._parse_result(site.read())
        num_wins = self.best_of / 2 + 1
        self.assertEqual(len(result[0]), num_wins)
        self.assertEqual(len(result[1]), num_wins)
        self.assertAlmostEqual(sum(result[0]) + sum(result[1]), 100, 1)

    def test_result_getter(self):
        """Tests the public getter method."""
        pass

if __name__ == "__main__":
    unittest.main()