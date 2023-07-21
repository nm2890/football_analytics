def compute_implied_odds(odds,model = 'uniform') :
  '''
  Compute estimated implied odds for bookmakers odds


  Parameters
  --------
  odds : list of decimal odds
  model : model used


  Available models :

  uniform : the margin is deduced in a uniform way for each odd

  proportional : the margin is proportional to odds, see




  Output
  -------
  odds_implied



  ## TO DO
  # Add more models !
  # Be able to deal with different odds format

  '''

  odds = np.array(odds)


  # ## Check if odds are > 1 , else return a list of nan
  # if not all(elem >= 1 for elem in odds) :
  #   return([np.nan]*len(odds))


  inv_odds = 1 / odds
  margin = np.sum(inv_odds,axis=1) - 1

  nb_odds = odds.shape[1]

  if model == 'uniform' :
    implied_odds = odds * np.reshape(1 + margin,(margin.shape[0],1))



  elif model == 'proportional' :
    implied_odds = nb_odds * odds / (nb_odds - np.reshape(margin,(margin.shape[0],1)) * odds)

  return(implied_odds)
