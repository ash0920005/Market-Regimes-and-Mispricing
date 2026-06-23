def calculate_ema(prices, period):
    alpha = 2 /(period + 1)
    ema = [0] * len(prices)
    sma = sum(prices[:period])/period
    ema[period - 1] = sma
    for i in range(period, len(prices)):
        ema[i] = prices[i]*alpha + ema[i-1] * (1-alpha)
    return ema
def calculate_macd(prices):
    ema12 = calculate_ema(prices,12)
    ema26 = calculate_ema(prices, 26)
    macd = []
    for i in range(len(prices)):
        macd.append(ema12[i] - ema26[i])
    return macd


def macd_signals(macd, signal):
    signals = [None] * len(macd)

    for i in range(1,len(macd)):
        if macd[i-1] < signal[i-1] and macd[i] > signal[i]:
            signals[i] = True

        elif macd[i-1] > signal[i-1] and macd[i] < signal[i]:
            signals[i] = False
    return signals

def calculate_rsi(prices, period=14):
    rsi = [None]*len(prices)
    gains = []
    losses = []
    for i in range(1,len(prices)):
        change = prices[i] - prices[i-1]
        gains.append(max(0,change))
        losses.append(max(0,-change))
    for i in range(period, len(gains)):
        avg_gain = sum(gains[i-period:i])/period
        avg_loss = sum(losses[i-period:i])/period
        if avg_loss == 0:
            rsi[i+1] = 100
            continue
        rs = avg_gain/avg_loss
        rsi[i+1] = 100 - (100/(rs+1))
    return rsi

    

