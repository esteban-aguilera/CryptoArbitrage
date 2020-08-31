import krakenex


# --------------------------------------------------------------------------------
# functions
# --------------------------------------------------------------------------------
def current_prices(symbol):
    """Get current bid and ask prices from kraken

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
    # Transform 'BTC' to 'XBT' as it is the convention used for Bitcoin in Kraken.
    symbol = symbol.replace('BTC', 'XBT')

    api = krakenex.API()
    req = api.query_public('Ticker', {'pair':symbol})
    
    try:
        data = req['result']
        data = data[list(data)[0]]
    except KeyError:
        Exception('No result. %s' % req['error'])
    
    # transform the string data to numbers
    bid, ask = float(data['b'][0]), float(data['a'][0])

    return bid, ask