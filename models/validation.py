from sklearn.metrics import log_loss
import numpy as np


def model_validation(y_true, y_pred, odds, bet_treshold):
    """
    Compute some metrics in order to evaluate a model


    Input
    --------
    y_true : binary np.array
    y_pred : np.array containing probability associated to event y_true == 1
    odds : odd offered by bookmakers for this event


    Output
    --------
    metrics_validation, a dict containing some validation metrics :
      - model_logloss : log loss of model prediction y_pred
      - bm_logloss : log loss deduced from bookmaker odds (with margin)
      - ROI : Return on investment based on bookmaker odds

    TO DO
    --------
    - implement non-flat stacking
    """

    metrics_validation = {}

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    odds = np.array(odds)
    prob_odds = 1 / odds

    # model and bm logloss
    metrics_validation['model_logloss'] = log_loss(y_true, y_pred)
    metrics_validation['bm_logloss'] = log_loss(y_true, prob_odds)

    # blind betting simulation
    gain = np.multiply(y_true, odds)
    pl = gain - 1
    metrics_validation['ROI_Blind'] = pl.sum() / len(pl)

    # betting on values
    odds_pred = [1 / pred for pred in y_pred]
    values = odds / odds_pred
    values_mask = values > bet_treshold
    y_true_values = y_true[values_mask]
    odds_values = odds[values_mask]
    gain = np.multiply(y_true_values, odds_values)
    pl = gain - 1
    metrics_validation['ROI_Model'] = pl.sum() / len(pl)

    return metrics_validation
