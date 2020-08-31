import os
import smtplib

from email.message import EmailMessage

# package imports
from .detector import arbitrage_opportunity


# --------------------------------------------------------------------------------
# functions
# --------------------------------------------------------------------------------
def arbitrage_msg(args):
    symbol = args['symbol']

    buy_at = args['buy_at']
    buy_price = args['buy_price']
    buy_comm = args['buy_comm']

    sell_at = args['sell_at']
    sell_price = args['sell_price']
    sell_comm = args['sell_comm']

    gain = args['gain']

    # create message
    msg = EmailMessage()
    msg['subject'] = 'Oportunidad de Arbitraje: BTC'
    msg['From'] = os.environ['EMAIL_ADDRESS']
    msg['To'] = os.environ['TO']

    # insert content to message
    msg.set_content(f"""Dear costumer,

Buy now {symbol} at {buy_at} for {buy_price} and sell them at {sell_at} for {sell_price}.  You will gain {100*gain}% !!

Best Regards,
Crypto Alert


--------------------------------------------------

The percentage of gain was calculated assuming a commision of {100*buy_comm}% at the moment of buying and
{100*sell_comm}% at the moment of selling.
""")

    return msg


def send_email(msg):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PASSWORD'])
        smtp.send_message(msg)


# --------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    args = arbitrage_opportunity('BTCEUR')
    if(args is not None):
        msg = arbitrage_msg(args)
        send_email(msg)
