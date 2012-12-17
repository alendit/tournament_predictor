Starcraft 2 tournament predictor
==================================

Uses data from `<aligulac.com`>_ to predict outcome of a tournament.

Example
---------

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