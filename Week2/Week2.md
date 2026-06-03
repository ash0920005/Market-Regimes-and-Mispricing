# Week 1
As proposed, we will be covering regression (and other time series modeling techniques) to find the relationship between two highly correlated datasets. You will also implement the Engle-Granger method to check whether the spread is stationary, and find the half-life of their mean reversion to generate signals.
Make sure to follow the content well at your own pace.

## Correlation (trap?)
A common pitfall in quantitative finance is assuming that two assets with a high correlation coefficient (like Pearson's $\rho$) can be traded as a mean-reverting pair. Correlation only measures the linear relationship between two variables over a specific time frame. Two tech stocks might both be trending upward in a bull market, yielding a correlation of 0.95. However, if their price difference (the spread) is not bounded, they can eventually diverge permanently, blowing up your account.

## The Engle-Granger Method
To mathematically prove that a pair is cointegrated, we rely on the Engle-Granger method. This transforms our two non-stationary price series into a single stationary series (the spread).

### But how?
1. OLS Regression: 
    We regress Asset A against Asset B to find the Hedge Ratio ($\beta$).   

        $$Y_t = \beta X_t + c + \epsilon_t$$

2. Once we have our hedge ratio, we isolate the residuals (the spread):
    $$\epsilon_t = Y_t - \beta X_t - c$$
    Now, we apply the Augmented Dickey-Fuller (ADF) test (which you built in Week 1) directly to the residuals $\epsilon_t$. If the ADF test yields a p-value $< 0.05$, we reject the null hypothesis. The residuals are stationary. $Y_t$ and $X_t$ are statistically cointegrated. We have found a tradable pair.

## OU process
Just because a spread is stationary doesn't mean it's tradable. If the spread takes 5 years to revert to its mean, our capital is locked up for too long. We need to calculate the speed of mean reversion.

### Modelling the spread
We model the stationary spread using the Ornstein-Uhlenbeck (OU) process, which mathematically describes a mean-reverting random walk in continuous time:

$$dz(t) = -\theta (z(t) - \mu) dt + \sigma dW$$

For our discrete daily data, we simplify this into a linear regression model:

$$\Delta z_t = -\theta z_{t-1} + \alpha + \epsilon_t$$

### Half-life:
Once you extract the slope $-\theta$ from your regression, you can calculate the half-life ($t_{1/2}$), which tells you the average number of days it takes for the spread to revert halfway back to its historical mean:

$$t_{1/2} = \frac{\ln(2)}{\theta}$$

The half-life period dictates the lookback window for your moving averages when you generate trading signals.

### Normalizing to Z-scores
We calculate the rolling mean ($\mu_{rolling}$) and rolling standard deviation ($\sigma_{rolling}$) of the spread. The window size for these rolling metrics should generally be close to the half-life you calculated earlier.

$$Z_t = \frac{\text{Spread}_t - \mu_{rolling}}{\sigma_{rolling}}$$

Now you have a normalized oscillator centered around zero. The trading rules are straightforward:
1. Long the Spread (Buy A, Sell $\beta$ of B): When $Z_t < -2.0$ (The spread is abnormally low and should revert upward)
2. Short the Spread (Sell A, Buy $\beta$ of B): When $Z_t > 2.0$ (The spread is abnormally high and should revert downward)
3. Exit Strategy: Close all positions when $Z_t$ crosses $0$ (The spread has reverted to the mean)

## Reading and Coding Assignment
Complete Chapter 3 of Ernie Chan's Algo Trading book. Make sure to try the solved examples in th chapter (use datasets from: [his website](https://epchan.com/book2))