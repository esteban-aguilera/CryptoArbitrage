import requests


# --------------------------------------------------------------------------------
# functions
# --------------------------------------------------------------------------------
def current_prices(symbol):
    """Get current bid and ask prices from cryptomkt

    Parameters
    ----------
    symbol: str
        Symbol used to represent the cryptocurrency exchange.  Example: BTCEUR.

    Returns
    -------
    bid: float
        Current bid value

    ask: float
        Current ask value.
    """
    # define constants
    url = 'https://api.cryptomkt.com/v1/ticker'
    payload = {'market': symbol}

    # generate request
    req = requests.get(url, params=payload).json()

    if(req['status'] == 'success'):
        # extract data from request
        data = req['data'][0]
        
        # transform bid and ask data from str to float.
        bid, ask = float(data['bid']), float(data['ask'])
    else:
        raise Exception(req['status'])

    return bid, ask