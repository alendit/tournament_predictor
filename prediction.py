"""This module contains the prediction class"""
from collections import defaultdict

class Prediction(object):
    """Prediction class. Represents a node in a prediction graph. 
    Dict of player aliases/ids and the probabilities, that the player
    advances at this point.
    """

    def __init__(init_dict=None, prediction_getter):
        self.prob_dict = init_dict or {}
        self.prediction_getter = prediction_getter

    def __getitem__(self, value):
        return self.prob_dict[value]

    def intersect(self, other_prob, best_of):
        """Crosses the predictions and get new probabilities"""
        assert isinstance(other_prob, Prediction)
        new_dict = defaultdict(float)
        for player1 in self.prob_dict.values():
            for player2 in self.prob_dict.values():
                direct_prob = self.prediction_getter.get_prediction(\
                    player1, player2, best_of)
                new_dict[player1] += direct_prob[0] * self.prob_dict[player1]\
                                        * other_prob[player2]
                new_dict[player2] += direct_prob[1] * other_prob[player2]\
                                        * self.prob_dict[player1]
