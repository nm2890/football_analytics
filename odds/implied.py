import numpy as np


def compute_implied_odds(odds, model='uniform'):

    """
    Compute estimated implied odds for bookmakers odds


    Input
    --------
    odds : array of decimal odds - size (nb_events,nb_odds)
    model : model used

    Available models :
    uniform : the margin is deduced in a uniform way for each odd
    proportional : the margin is proportional to odds, see https://www.football-data.co.uk/The_Wisdom_of_the_Crowd.pdf

    Output

    -------
    array of odds_implied - size (nb_events,nb_odds)

    TO DO
    -------
    - Add more models !
    - Be able to deal with different odds format
    - check if all odds are in acceptable format
    - proportional model returns uncoherent results (odd < 0) when BM odd >> 30
    """

    odds = np.array(odds)

    inv_odds = 1 / odds
    margin = np.sum(inv_odds, axis=1) - 1
    nb_odds = odds.shape[1]

    if model == 'uniform':
      implied_odds = odds * np.reshape(1 + margin, (margin.shape[0], 1))
    elif model == 'proportional':
      implied_odds = np.multiply(nb_odds,odds) / (nb_odds - np.multiply(np.reshape(margin, (margin.shape[0], 1)) , odds))
    else :
      raise Exception(f"Model {model} not implemented")

    return (implied_odds)
