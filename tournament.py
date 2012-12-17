'''
Tournament module
'''
import simplejson
from prediction import Prediction


class Tournament(object):
    """Represents a play off tournament"""

    def __init__(self, bracket, predictor):
        self.bracket = bracket
        self.predictor = predictor

    def calculate_prediction(self):
        """Does the actual calculation"""
        return self._recursive_prediction(self.bracket)

    def _recursive_prediction(self, bracket_position):
        """Recieves a list representing a bracket position,
        calculates predictions recursively"""
        predictions = []
        assert (len(bracket_position) == 3)
        for child in bracket_position[:-1]:
            if isinstance(child, str):
                predictions.append(Prediction({child: 1}))
            else:
                predictions.append(self._recursive_prediction(child))
        return predictions[0].intersect(predictions[1], bracket_position[2],
                                        self.predictor)

    @classmethod
    def from_json(cls, path, predictor):
        """Loads tourmanet description json file from path
        and returns a Tourmantent instance"""
        try:
            with open(path, 'r') as bracket_file:
                return cls(simplejson.load(bracket_file)['tournament'],
                           predictor)
        except IOError as error:
            raise
