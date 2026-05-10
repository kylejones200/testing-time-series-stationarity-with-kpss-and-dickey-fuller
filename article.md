# Testing Time Series Stationarity with KPSS and Dickey-Fuller Time series analysis often begins with determining whether a series is
stationary --- its statistical properties, like mean and variance, do...

### Testing Time Series Stationarity with KPSS and Dickey-Fuller
#### Two approaches to verify if your time series data is stationary before analysis
Time series analysis often begins with determining whether a series is **stationary** --- its statistical properties, like mean and variance, do not change over time. Our task today is to use the **KPSS test** and the **Dickey-Fuller test** to identify if the series is stationarity. These tests begin with different assumptions (KPSS assumes the data is not stationary and Dickey-Fuller assumes the data is stationary).

### Stationarity in Time Series
A stationary time series has a **constant mean (**The average value doesn't drift over time), **constant variance (**The spread of the data remains stable) and **no seasonality (T**he data shows no regular patterns or cycles).

Stationarity matters because many time series models assume the input data is stationary (like ARIMA).


<figcaption>Key Differences Between KPSS and Dickey-Fuller Tests</figcaption>


Let's generate and analyze a stationary time series and a non-stationary time series to test these tests.




**Stationary Series**:

- KPSS test typically fails to reject the null hypothesis (p-value \> 0.05), confirming stationarity.
- Dickey-Fuller test rejects the null hypothesis (p-value \< 0.05), also confirming stationarity.


**Non-Stationary Series**:

- KPSS test rejects the null hypothesis (p-value \< 0.05), indicating non-stationarity.
- Dickey-Fuller test fails to reject the null hypothesis (p-value \> 0.05), also indicating non-stationarity.


### When to Use Each Test
- Use **KPSS** to test whether a time series is stationary around a deterministic trend.
- Use **Dickey-Fuller** to test for unit roots (random walks) and ensure stationarity for ARIMA modeling.

Since these tests approach stationarity from different angles, it's common to use both for a more comprehensive analysis.

### So what?
Stationarity is a basic concept in time series modeling. The KPSS and Dickey-Fuller tests give us two different approaches to assess stationarity and decide on appropriate transformations (e.g., differencing) to stabilize the series.

### Thank you for being a part of the community
*Before you go:*

- Be sure to **clap** and **follow** the writer ️👏**️️**
- [Follow us: [**X**](https://x.com/inPlainEngHQ) \| [**LinkedIn**](https://www.linkedin.com/company/inplainenglish/) \| [**YouTube**](https://www.youtube.com/channel/UCtipWUghju290NWcn8jhyAw) \| [**Newsletter**](https://newsletter.plainenglish.io/) \| [**Podcast**](https://open.spotify.com/show/7qxylRWKhvZwMz2WuEoua0)]
- [[**Check out CoFeed, the smart way to stay up-to-date with the latest in tech**](https://cofeed.app/) **🧪**]
- [[**Start your own free AI-powered blog on Differ**](https://differ.blog/) 🚀]
- [[**Join our content creators community on Discord**](https://discord.gg/in-plain-english-709094664682340443) 🧑🏻‍💻]
- [For more content, visit [**plainenglish.io**](https://plainenglish.io/) + [**stackademic.com**](https://stackademic.com/)]
