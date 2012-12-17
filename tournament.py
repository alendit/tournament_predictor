'''
"Usage: python tournament.py <json_description.json>"
'''
import sys
import simplejson
from prediction import Prediction
from prediction_getter import WebPredictor


class Tournament(object):
    """Represents a play off tournament"""

    def __init__(self, bracket):
        self.bracket = bracket

    def calculate_prediction(self, prediction_getter):
        """Does the actual calculation"""
        self.prediction_getter = prediction_getter
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
                                        self.prediction_getter)

    @classmethod
    def from_json(cls, path):
        """Loads tourmanet description json file from path
        and returns a Tourmantent instance"""
        try:
            with open(path, 'r') as bracket_file:
                return cls(simplejson.load(bracket_file)['tournament'])
        except IOError as error:
            print error
            raise

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print __doc__
        sys.exit(1)
    else:
        tournament = Tournament.from_json(sys.argv[1])
        prediction_getter = WebPredictor()
        print tournament.calculate_prediction(prediction_getter)
