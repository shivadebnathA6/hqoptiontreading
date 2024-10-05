
import pandas as pd

def backtest_strategy(data, strategy_function, **kwargs):
    data['Signal'] = strategy_function(data, **kwargs)
    data['Returns'] = data['close'].pct_change()
    data['Strategy Returns'] = data['Signal'].shift(1) * data['Returns']
    cumulative_returns = (1 + data['Strategy Returns']).cumprod() - 1
    return cumulative_returns

def example_strategy(data, threshold=0.01):
    signal = (data['close'].pct_change() > threshold).astype(int)
    return signal

if __name__ == "__main__":
    data = pd.read_csv('historical_data.csv')
    cumulative_returns = backtest_strategy(data, example_strategy, threshold=0.01)
    print(cumulative_returns.tail())
