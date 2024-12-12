import ccxt
import pandas as pd
import matplotlib.pyplot as plt

# Initialize the Binance exchange
exchange = ccxt.binance()

# Fetch the last 100 1-minute candlesticks for BTC/USDT
symbol = 'BTC/USDT'
timeframe = '1m'
data = exchange.fetch_ohlcv(symbol, timeframe, limit=100)

# Convert the data to a DataFrame
columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(data, columns=columns)
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Plot the closing prices
plt.plot(df['timestamp'], df['close'])
plt.title('BTC/USDT Closing Prices')
plt.xlabel('Time')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.show()
