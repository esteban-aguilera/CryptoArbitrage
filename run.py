import os
import time


# package imports
from crypto_arbitrage.detector import arbitrage_opportunity
from crypto_arbitrage.communicator import arbitrage_msg, send_email


# --------------------------------------------------------------------------------
# environment variables
# --------------------------------------------------------------------------------
os.environ['EMAIL_ADDRESS'] = 'origin email address'
os.environ['EMAIL_PASSWORD'] = 'destiny email address'
os.environ['TO'] = 'destination email address'


# --------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------
def main():
    # show possible arbitrage opportunities!
    pairs = ['BTCEUR', 'ETHEUR', 'EOSEUR', 'XLMEUR']
    for i, pair in enumerate(pairs):
        if(i != 0):
            time.sleep(5)  # don't overload APIs
        
        args = arbitrage_opportunity(pair)
        if(args is not None):
            if(100*args['gain'] > 1.0):
                # gains are greater the 1%
                msg = arbitrage_msg(args)
                
                print(msg, 5*'\n')
                # # Must set os.environ use this functions
                # send_email(msg)



# --------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    main()