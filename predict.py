'''
Usage: python tournament.py <json_description.json>
'''
import sys
from prediction_getter import WebPredictor
from tournament import Tournament


def main():
    """Main predict method"""
    if len(sys.argv) != 2:
        print __doc__
        sys.exit(1)
    else:
        tournament = Tournament.from_json(sys.argv[1])
        prediction_getter = WebPredictor()
        print tournament.calculate_prediction(prediction_getter)


if __name__ == "__main__":
    main()
