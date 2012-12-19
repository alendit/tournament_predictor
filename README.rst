Starcraft 2 tournament predictor
==================================

Uses data from `<aligulac.com`>_ to predict outcome of a tournament.

.. topic:: Notice!

    The developer of aligulac.com has a much advanced project which you can find at https://github.com/TheBB/simul .
    There will be no futher development in this project!

Example
---------

Get predictions for a dummy-tournament (from test_tournament)::

    python predict test_tournament.json

JSON tournamen format
-----------------------

The JSON object::

    {'tournament' : <bracket-stage>}

Each bracket stage is represented by::

    [
        <player1-id>|<left-bracket-stage>,
        <player2-id>|<right-bracket-stage>,
        <best-of-number>
    ]
