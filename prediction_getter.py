import urllib
import urllib2
from pyquery import PyQuery

from IPython import embed


class WebPredictor(object):
    """Gets predicted results from aligulac.com.
    Implements get_predictions method"""

    PREDICTIONS_URL = "http://aligulac.com/predict/match/"

    def get_predictions(self, player1, player2, best_of):
        """Sends request to aligulac.com to get a single bestof prediction"""

        pass

    def _get_page(self, player1, player2, best_of):
        data = {"p1": player1,
                "p2": player2,
                "bo": best_of,
                }

        site = urllib2.urlopen("{}?{}".format(\
            self.PREDICTIONS_URL, urllib.urlencode(data)))
        return site

    def _parse_result(self, html):
        """Takes a result html page and returns probabillities
        of winning for 2 players in format:
         ([prob_p1_0_loss, prob_p1_1_loss, ...],
           [prob_p2_0_loss, ...])
        """

        result = ([], [])

        page = PyQuery(html)
        table = PyQuery(page("div.table")[0])
        for row in table(".row"):
            row = PyQuery(row)
            player1_prob = self._get_prob_from_rowe(row(".rowe")[0])
            player2_prob = self._get_prob_from_rowe(row(".rowe")[-1])
            result[0].append(player1_prob)
            result[1].append(player2_prob)

        return result

    def _get_prob_from_rowe(self, html):
        """Takes html and return probability in float"""
        return float(html.text.strip().replace("%", ""))

