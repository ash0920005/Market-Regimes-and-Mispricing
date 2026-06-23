import pandas as pd
import indicators
import filters
df = pd.read_csv("stocks.csv")
prices = df['Close'].to_list()
volumes = df['Volume'].to_list()

def final_strategy(prices, volumes):
    macd = indicators.calculate_macd(prices)
    signal_line = indicators.calculate_ema(macd,9)
    macd_signal = indicators.macd_signals(macd,signal_line)
    rsi = indicators.calculate_rsi(prices)
    vol_ok = filters.volume_filter(volumes)
    signals = []
    for i in range(30,len(macd)):
        m = macd_signal[i]
        r = (rsi[i] is not None) and (rsi[i] < 70)
        v = vol_ok[i]
        if m and r and v:
            signals.append(i)
    return signals


