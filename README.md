# Testing Time Series Stationarity with KPSS and Dickey Fuller

Published: 2025-01-20
Medium: [https://medium.com/@kyle-t-jones/testing-time-series-stationarity-with-kpss-and-dickey-fuller-42fbee097d37](https://medium.com/@kyle-t-jones/testing-time-series-stationarity-with-kpss-and-dickey-fuller-42fbee097d37)

## Business context

Time series analysis often begins with determining whether a series is stationary --- its statistical properties, like mean and variance, do not change over time. Our task today is to use the KPSS test and the Dickey-Fuller test to identify if the series is stationarity. These tests begin with different assumptions (KPSS assumes the data is not stationary and Dickey-Fuller assumes the data is stationary).

A stationary time series has a constant mean (The average value doesn't drift over time), constant variance (The spread of the data remains stable) and no seasonality (The data shows no regular patterns or cycles).

Stationarity matters because many time series models assume the input data is stationary (like ARIMA).

## About

Place the code for this article in this repository.
The original article export is saved as `article.md`.

## Files

Add your `.ipynb`, `.py`, `.yaml`, `.js`, `.ts`, or other project files here.

## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).