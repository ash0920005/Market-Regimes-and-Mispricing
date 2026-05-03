# Market Regimes and Mispricing
<img width="250" height="150" alt="Screenshot 2026-05-03 230317" src="https://github.com/user-attachments/assets/d3aa1708-d40f-4d5b-8cd3-2ea30d91ed59" />

## Description

This project is all about using pure mathematics to figure out what the market is doing, and then deploying the right algorithm to exploit it. You'll build a regime classifier using statistical tests to prove whether an asset is trending or mean-reverting mathematically. Based on that, your code will dynamically switch between a pairs trading model for mean-reverting time series and a momentum model for trend-following time series. Finally, we'll tackle risk and learn how to hedge out Beta -the broader stock market's movements- so that your algorithm generates Alpha (uncorrelated profit).
### Suggested Resources
As for suggested resources, Ernie Chan's book on Algorithmic Trading and Kahn's book on Active Portfolio Management are recommended.
## Proposed Timeline
* In Week 1, we intend to cover time-series statistics and conduct tests for stationarity, such as the ADF test. You will also apply the Hurst exponent to categorise our time series as mean-reverting, random walk or trending.
* In Week 2, we will be covering regression (and other time series modelling techniques) to find the relationship between two highly correlated datasets. You will also implement the Engle-Granger method to check whether the spread is stationary, and find the half-life of their mean reversion to generate signals.
* In Week 3, we will build momentum indicators to catch breakouts and write filters to ignore short-term market noise and avoid signals if they are false.
* Week 4 will be about isolating the alpha. You'll learn about CAPM (Capital Asset Pricing Model) and use regression (against a benchmark) to calculate the algo's beta and calculate the short positions needed to hedge our portfolio to market-neutral, leaving only pure Alpha. 
* In Week 5, we will combine all that we covered in the previous weeks and develop a (hopefully, vectorised) backtester to develop a combined strategy. We'll wrap up by implementing the Kelly Criterion for optimal bet sizing and generating performance metrics (Sharpe ratio, max drawdown, win rate).
## Project Checkpoints
1) A working module to input data and output Hurst Exponents to dictate which trading algorithm to utilise
2) Successful identification of a cointegrated asset pair and calculation of its mean-reversion half-life to generate precise Z-score entry/exit signals
3) A functioning trend-following algorithm that captures sustained price movements while filtering out fakeouts
4) A risk-management module that calculates the portfolio's Beta and hedges it to zero
5) A completed backtest free of look-ahead bias, that utilises the Kelly criterion for position sizing.
