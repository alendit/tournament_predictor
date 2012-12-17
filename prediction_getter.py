import urllib
import urllib2
from pyquery import PyQuery

from IPython import embed
from prediction import Prediction


class WebPredictor(object):
    """Gets predicted results from aligulac.com.
    Implements get_predictions method"""

    PREDICTIONS_URL = "http://aligulac.com/predict/match/"

    def get_predictions(self, player1, player2, best_of):
        """Sends request to aligulac.com to get a single bestof prediction"""

        probabilities = self._parse_result(self._get_page(player1,
                                                    player2, best_of))
        win_probabilities = {
                             player1: sum(probabilities[0]) / 100.,
                             player2: sum(probabilities[1]) / 100.,
                             }
        return Prediction(win_probabilities)

    def _get_page(self, player1, player2, best_of):
        """Return a prediction page"""
        data = {"p1": player1,
                "p2": player2,
                "bo": best_of,
                }

        site = urllib2.urlopen("{}?{}".format(\
            self.PREDICTIONS_URL, urllib.urlencode(data)))

        page = PyQuery(site.read())

        if len(page("input[type='radio']")) > 0:
            page = self._get_unique_players(page, player1, player2, best_of)

        return page

    def _get_page_by_ids(self, player1_id, player2_id, best_of):
        data = {"i1": player1_id,
                "i2": player2_id,
                "bo": best_of,
                }

        site = urllib2.urlopen("{}?{}".format(\
            self.PREDICTIONS_URL, urllib.urlencode(data)))
        return site

    def _parse_result(self, page):
        """Takes a result html page and returns probabillities
        of winning for 2 players in format:
         ([prob_p1_0_loss, prob_p1_1_loss, ...],
           [prob_p2_0_loss, ...])
        """

        result = ([], [])

        table = PyQuery(page("div.table")[0])
        for row in table(".row"):
            row = PyQuery(row)
            player1_prob = self._get_prob_from_rowe(row(".rowe")[0])
            player2_prob = self._get_prob_from_rowe(row(".rowe")[-1])
            result[0].append(player1_prob)
            result[1].append(player2_prob)

        return result

    def _get_unique_players(self, html, player1, player2, best_of):
        """Called whene there are multiple players with the same nickname"""
        player_rows = PyQuery(html)(".row")[:2]
        player_names = (player1, player2)
        player_ids = []
        for player_row, player_name in zip(player_rows, player_names):
            row = PyQuery(player_row)
            if len(row("input[type='radio']")) == 1:
                player_ids.append(row("input[type='radio']").val())
            else:
                possible_players = [(PyQuery(nickname).text(), PyQuery(player_id).val()) \
                    for nickname, player_id in zip(
                        row("a"),
                        row("input[type='radio']"),
                                                    )]
                player_ids.append([(player_nickname, player_id) \
                    for player_nickname, player_id in possible_players\
                    if player_nickname == player_name][0][1])

        player1_id, player2_id = player_ids
        site = self._get_page_by_ids(player1_id, player2_id, best_of)
        return PyQuery(site.read())

    def _get_prob_from_rowe(self, html):
        """Takes html and return probability in float"""
        return float(html.text.strip().replace("%", ""))
