# Week 1

As proposed we'll cover time-series statistics and conduct tests for stationarity and apply the Hurst exponent to categorise our time series as mean-reverting, random walk or trending.
Make sure to follow the content well at your own pace.

## Time-series statistics

### What's the frequency, Kenneth?
1. A time series is simply a sequence of data points indexed in chronological order: $X_t$ for $t \in \{1, 2, \dots, T\}$.Examples include a company’s quarterly sales, daily stock returns, or monthly currency exchange rates. 
Unlike standard cross-sectional data, time-series observations are inherently dependent on their own past.
2. Characteristics of a time series:
    - **Trend:** The long-term drift or structural directional movement in the data.
    - **Seasonality:** Predictable, periodic fluctuations that repeat within a specific calendar window (e.g., the "weekend effect" or intraday volume smiles).
    - **Volatility Clustering:** The tendency for high-volatility events to cluster together (shocks generate more shocks, a phenomenon famously modeled by ARCH/GARCH processes).
    - **Non-linearity:** Structural breaks and regime shifts that make life miserable for simple linear models.

        You can watch [this introduction to time-series decomposition](https://youtu.be/GE3JOFwTWVM?si=ejA-RpfaKJ4nvE6s)

### Stationarity? Stationarity?? or Stationarity???
Stationarity is important because it implies that the statistical properties of the data generation process do not change over time - making it predictable.

#### 1. First-Order (or weak) Stationarity
It requires only that the expected value (mean) of the series remains constant over time:
$$\mathbb{E}[X_t] = \mu \quad \forall t$$
Note that the variance, skewness, and other higher moments can wildly drift. 

#### 2. Weak (Second-Order / Covariance) Stationarity
It requires that the mean and variance stay the same throughout, and the relationship between data points (that is autocovariance) is a function $\Delta{t}$ (how far apart they are in time, not when they occur.)
So, a process is weakly stationary if it satisfies three strict conditions:
1.  **Constant Mean:** $\mathbb{E}[X_t] = \mu$ for all $t$.
2.  **Finite Variance:** $\mathbb{E}[X_t^2] < \infty$ 
3.  **Time-Invariant Autocovariance:** 
$$\text{Cov}(X_t, X_{t+\tau}) = \gamma(\tau) \quad \text{where} \quad \Delta t = \tau$$

#### 3. Strict Stationarity
A process is strictly stationary if the entire *joint distribution* of any subsequence of data points remains completely invariant to time shifts. Formally, for any choice of $t_1, \dots, t_k$ and any shift $\tau$:
$$F_{X_{t_1}, \dots, X_{t_k}}(x_1, \dots, x_k) = F_{X_{t_1+\tau}, \dots, X_{t_k+\tau}}(x_1, \dots, x_k)$$
This implies that every single statistical moment (mean, variance, skewness, kurtosis, etc.) is a constant. 
* If you don't know moments and MGFs you can check out [this lecture](https://youtu.be/N8O6zd6vTZ8?si=8yTM7s2JqhJk1ugq) but dw we won't need full MGF derivations

In the real world, asset prices ($P_t$) are almost **never** stationary. They drift, trend, and explode. Therefore, our goal is rarely to find an inherently stationary asset, but rather to construct a stationary variation or combination of the series.

**Example!** 

Suppose the time series is:

$$
y_t = \beta_0 + \beta_1 t + \varepsilon_t
$$

This series is **not stationary** because the mean changes over time due to the trend component. Define a new series as:

$$
z_t = y_t - y_{t-1}
$$

Substitute the expressions for \(y_t\) and \(y_{t-1}\):

$$
z_t = (\beta_0 + \beta_1 t + \varepsilon_t) - (\beta_0 + \beta_1 (t-1) + \varepsilon_{t-1})
$$

$$
z_t = \beta_0 + \beta_1 t + \varepsilon_t - \beta_0 - \beta_1 t + \beta_1 - \varepsilon_{t-1}
$$

$$
z_t = \beta_1 + (\varepsilon_t - \varepsilon_{t-1})
$$

Since:

$$
E(\varepsilon_t) = 0
$$

then:

$$
E(z_t) = \beta_1
$$

Assuming the errors are independent:

$$
Var(z_t) = Var(\varepsilon_t - \varepsilon_{t-1}) = 2\sigma^2
$$
Hence, using first differencing, this series is stationary.

---
*Note* Make sure you know what (partial and otherwise) auto-correlation functions are. [Check this](https://youtu.be/DeORzP0go5I?si=puqfWLJoZbMq3vjz)

---

#### Transformations:
We know stationary data sets are very useful, hence we come up with various methods to transform a non-stationary time series to stationary one. 

- **Differencing**: One of the most common methods. You take the difference between consecutive data points over multiple iterations if needed.
- **Detrending**: Fit a trend line to your data (linear or nonlinear), then analyze the leftover part (the residuals), which is often stationary.
- **Smoothing and Transformations**: Techniques like taking the logarithm or square root of the data can help stabilise the variance and make the series more predictable.
---

### Some cleaning ;)

Before we conduct any tests we need to make sure that our data is "nice and smooth." After sourcing the data, make sure you clean it (like trying to handle NaNs (*how will you do that?*))

*Note*: Also read [survivor bias!](https://en.wikipedia.org/wiki/Survivorship_bias)

#### Cookbook


---
### It's a Non-Stationary Truth!
There are a number of ways to test if your time series is stationary:
1. **Unit Root Tests**: Tests like the Augmented Dickey-Fuller (ADF) and Zivot-Andrews are used to see if the series has a unit root, which is a red flag for non-stationarity.

2. **KPSS Test**: This test works a bit differently - it checks if the series is stationary around a trend or needs differencing to become stationary. While ADF checks for non-stationarity, KPSS checks for stationarity so together they provide a more complete picture.

3. **Run Sequence Plots**: A simple but effective visual method. These plots show the data over time and help spot trends or seasonal patterns.

4. **Less Common Tests**: There are more advanced methods like the Priestley-Subba Rao test or wavelet-based techniques, which are used in more specialised scenarios.

Please go through [this notion page that we created](https://www.notion.so/pantalaimon/It-s-a-non-stationary-truth-367b2bd16afa800d9887fd4e72e89d79?source=copy_link) to get to know the above methods.


## Hurst who?

Please go through [this notion page that we created](https://www.notion.so/pantalaimon/It-s-a-non-stationary-truth-367b2bd16afa800d9887fd4e72e89d79?source=copy_link#367b2bd16afa80e98835cf5430154ecd) to get to know about this.

---
## Reading and coding assignment
- Section 18.8 from Paul Wilmott on Quantitative Finance
- Chapter 2 from Ernie Chan’s book