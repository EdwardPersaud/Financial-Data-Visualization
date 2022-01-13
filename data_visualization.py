# MGS314 Final Project
#Edward Persaud

# Importing all of the modules necessary for creating CSV files and graphing
import pandas_datareader as web
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

# Each companies stock market ticker, you can search for stock tickers online for any public company
companies = ['AAPL','MSFT','FISV', 'SNAP']

# Any given time period 
start = dt.datetime(2015,1,1)
end = dt.datetime(2022,1,1)
 
#Create CSV file for each company using data from Yahoo Finance
for i in companies:
    df = web.DataReader(i, 'yahoo', start, end)
    data = df.to_csv(i + '.csv')

# Change the style for each graph
style.use('dark_background')

# Draw graphs for each company 
for i in companies:
    df = pd.read_csv(i + '.csv', parse_dates = True, index_col = 0)
    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
    df.dropna(inplace=True)
 
    # Adjusted close graph
    df['Adj Close'].plot(color = 'red')
    plt.title(i + ' Adjusted Close')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()
    
    # 100 day moving average
    df['100ma'].plot(color = 'green')
    plt.title(i + ' 100-Day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()
    
    # Volume graph
    df['Volume'].plot(color = 'blue')
    plt.title(i + ' Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.show()
    
    # Generates a table in the shell
    print(df[['High', 'Low', 'Adj Close']].tail(20))
