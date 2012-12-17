"""This module contains the prediction class"""
from collections import defaultdict, OrderedDict


class Prediction(dict):
    """Prediction class. Represents a node in a prediction graph. 
    Dict of player aliases/ids and the probabilities, that the player
    advances at this point.
    """

    def intersect(self, other_prob, best_of, prediction_getter):
        """Crosses the predictions and get new probabilities"""
        assert isinstance(other_prob, Prediction)
        new_dict = defaultdict(float)
        for player1 in self:
            for player2 in other_prob:
                direct_prob = prediction_getter.get_predictions(\
                    player1, player2, best_of)
                new_dict[player1] += direct_prob[player1] * self[player1]\
                                        * other_prob[player2]
                new_dict[player2] += direct_prob[player2] * \
                            other_prob[player2] * self[player1]

        return Prediction(new_dict)

    def __repr__(self):
        ordered_dict = OrderedDict(sorted(self.items(), key=lambda t: t[1],
                                          reverse=True))
        return repr(ordered_dict)
