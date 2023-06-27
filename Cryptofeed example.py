from cryptofeed import FeedHandler
from cryptofeed.exchanges import Coinbase, BinanceUS
from cryptofeed.defines import TRADES, TICKER, L2_BOOK, BID, ASK
from cryptofeed.backends.mongo import BookMongo #, TradeMongo, TickerMongo
import datetime
import pandas as pd
import matplotlib.pyplot as plt

i = 0

val1 = 'BTC' # put the actual crypto here
val2 = 'USD' # val2 is generaly for the 

async def ticker(t, receipt_timestamp):
    print(t)

async def trade(t, receipt_timestamp):
    print(t)

async def book(t, receipt_timestamp):
    global i
    i+=1
    print(f'{i} - Timestamp: {t.timestamp} Exchange: {t.exchange} Symbol: {t.symbol} Book Bid Size is {len(t.book[BID])} Ask Size is {len(t.book[ASK])}')
    
    ob = t.book.bids.to_dict()
    bids = tuple((float(k), float(v)) for k, v in ob.items())
    bids = pd.DataFrame(bids)

    ob = t.book.asks.to_dict()
    asks = tuple((float(k), float(v)) for k, v in ob.items())
    asks = pd.DataFrame(asks)

    bids.columns = ['Price', 'Size']
    asks.columns = ['Price', 'Size']

    # for price in ob.book.bids:
    #     print(f"{i} - Price: {price} Size: {ob.book.bids[price]}")

    print(f'Asks: \n{asks}\n')
    print(f'Bids: \n{bids}')

    ###### Un-comment the code below to see a visualization of the orderbook at every update ######
    ''' 
    plt.bar(asks['Price'], asks['Size'],  color='b', alpha=0.5, label='asks', width=0.01)
    plt.bar(bids['Price'], bids['Size'],  color='r', alpha=0.5, label='bids', width=0.01)
    plt.xlabel(f'Price {val1}-{val2}')
    plt.ylabel(f'{val1} Quantity')
    plt.legend()
    plt.show()
    '''

def main():
    f = FeedHandler()
    f.add_feed(BinanceUS(symbols=[f'{val1}-{val2}'], channels=[L2_BOOK], callbacks={L2_BOOK: book,},))
    f.run()
    
if __name__ == '__main__':
    main()
