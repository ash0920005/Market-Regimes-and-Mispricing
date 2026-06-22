# Week 4

Week 4 focuses entirely on isolating the alpha. You will learn about CAPM (Capital Asset Pricing Model) and use regression against a benchmark to calculate the algorithm's beta. We aim to build a risk-management module that calculates the portfolio's Beta and hedges it to zero.

Again make sure to go through the material at your own pace, and don't hesitate to reach out to us in case of any problems.

## The Capital Asset Pricing Model (CAPM)

### Deconstructing Returns
CAPM is a foundational financial model that establishes a linear relationship between the expected return of an investment and its systemic risk.

The expected return of an asset $E[R_i]$ is given by:
$$E[R_i] = R_f + \beta_i (E[R_m] - R_f) + \alpha_i$$

Where:
* $R_f$ is the risk-free rate.
* $\beta_i$ is the sensitivity of the asset's returns to the broader market.
* $E[R_m]$ is the expected return of the market benchmark.
* $\alpha_i$ is the asset's unique, risk-adjusted performance—our pure Alpha.

Beta represents returns explained by market movement. If a strategy has a beta of 1.2 and the market rises by 10%, we expect roughly 12% of the strategy's return to come from market exposure alone.

Alpha is the portion of return that cannot be explained by market exposure and represents genuine strategy skill.

### Finding Beta through Regression
To isolate alpha, we first define our beta. We use linear regression to find the slope of our asset's returns against the benchmark's returns. 

The regression equation is:

$$R_i = \alpha + \beta R_m + \epsilon$$

where:
* $R_i$ is the asset return
* $R_m$ is the benchmark return
* $\alpha$ is the intercept (Alpha)
* $\beta$ is the slope (Beta)
* $\epsilon$ is the unexplained residual

Mathematically, Beta is also calculated as the covariance of the asset and market returns, divided by the variance of the market returns:
$$\beta = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)}$$

## Hedging for Market Neutrality
If the broader market crashes, a well-hedged strategy should be significantly less affected than an unhedged strategy.

Once we know the portfolio Beta, we calculate the exact lot sizes required to short the benchmark (e.g., SPY). By offsetting this systemic exposure until $\beta_{portfolio} \approx 0$, the remaining returns become largely independent of market direction.

## Reading and Coding Assignment

### Reading
Read the following Investopedia articles:

- [CAPM (Capital Asset Pricing Model)](https://www.investopedia.com/terms/c/capm.asp?)
- [Alpha](https://www.investopedia.com/terms/a/alpha.asp?)
- [Beta](https://www.investopedia.com/terms/b/beta.asp?)
- [Market Neutral Strategies](https://www.investopedia.com/terms/m/marketneutral.asp?)

### Coding
You are expected to implement risk_management.py, which should calculate asset and benchmark returns, estimate beta using linear regression, and finally compute the hedge ratio required to reduce portfolio Beta.
To test your implementation, you may use any asset and benchmark pair form the datasets available on the previously mentioned website.