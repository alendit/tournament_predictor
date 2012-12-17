'''
Created on Dec 17, 2012

@author: alendit
'''
import simplejson


class Tournament(object):
    """Represents a play off tournament"""

    def __init__(self, bracket):
        self.bracket = bracket

    def calculate_probabilities(self):
        """Does the actual calculation"""
        pass

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
