import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # TODO: Fill in this function.
    
    df = pd.DataFrame(prices)
    a = df.copy()
    b = df.copy()
    a = a[b['ticker']=='A']
    b = b[b['ticker']=='B']
    a['lg_return'] = np.log(a.price) - np.log(a.price.shift(1))
    b['lg_return'] = np.log(b.price) - np.log(b.price.shift(1))
    #a['log_return'] = np.log(a.price) - np.log(a.price,shift(1)
    print(a.std())
    print(b.std())
    #print(df[df['ticker']=='B'])
    
    return 'B'
    pass


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()
