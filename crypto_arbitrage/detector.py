# package imports
from .api_managers import cryptomkt, kraken


def arbitrage_opportunity(symbol, **kwargs):
    """Gets arbitrage opportunity for a particular symbol between two
    different exchanges.

    Parameters
    ----------
    symbol: str
        Symbol used to represent the cryptocurrency exchange.  Example: BTCEUR.

    Returns
    -------
    orders: dict or None
        Dictionary with the arguments needed to describe completely the
        arbitrage opportunity.  It has the keys 'buy_at', 'buy_price',
        'buy_comm', 'sell_at', 'sell_price', 'sell_comm' and 'gain'.
        If there is no arbitrage oportunity, it returns None.
    """
    sources = kwargs.get('sources', ['kraken', 'cryptomkt'])
    commissions = kwargs.get('commissions', [0.26, 0.68])
    
    args = arbitrage_result(symbol,
        buy_at=sources[0] , buy_comm=commissions[0],
        sell_at=sources[1], sell_comm=commissions[1]
    )
    if(args['gain'] > 0):
        return args
    
    args = arbitrage_result(symbol,
        buy_at=sources[1] , buy_comm=commissions[1],
        sell_at=sources[0], sell_comm=commissions[0]
    )
    if(args['gain'] > 0):
        return args
    
    return None


def arbitrage_result(symbol, **kwargs):
    """Calculates the gains from performing arbitrage between two
    different cryptocurrency exchanges.

    Parameters
    ----------
    symbol: str
        Symbol used to represent the cryptocurrency exchange.  Example: BTCEUR.

    Returns
    -------
    args: dict
        Dictionary with the arguments needed to describe completely the
        arbitrage opportunity.  It has the keys 'buy_at', 'buy_price',
        'buy_comm', 'sell_at', 'sell_price', 'sell_comm' and 'gain'.
    """
    buy_at = kwargs.get('buy_at', 'kraken').lower()
    buy_comm = kwargs.get('buy_comm', 0.26) / 100
    buy_bid, buy_ask = current_prices(symbol, buy_at)
    
    sell_at = kwargs.get('sell_at', 'cryptomkt').lower()
    sell_comm = kwargs.get('sell_comm', 0.68) / 100
    sell_bid, sell_ask = current_prices(symbol, sell_at)

    gain = (sell_bid*(1-sell_comm)-buy_ask*(1+buy_comm))/(buy_ask*(1+buy_comm))
        
    args = {
        'symbol':symbol,
        'buy_at':buy_at,
        'buy_price':buy_ask,
        'buy_comm':buy_comm,
        'sell_at':sell_at,
        'sell_price':sell_bid,
        'sell_comm':sell_comm,
        'gain':gain
    }

    return args
    

def current_prices(symbol, source, **kwargs):
    """Get current bid and ask prices for a symbol from a source.

    Parameters
    ----------
    symbol: str
        Symbol used to represent the cryptocurrency exchange.  Example: BTCEUR.

    source: str
        Source used to obtain bid and ask values.

    Returns
    -------
    bid: float
        Current bid value.

    ask: float
        Current ask value.
    """
    source = source.lower()
    if(source == 'cryptomkt'):
        bid, ask = cryptomkt.current_prices(symbol)
    elif(source == 'kraken'):
        bid, ask = kraken.current_prices(symbol)

    return bid, ask
