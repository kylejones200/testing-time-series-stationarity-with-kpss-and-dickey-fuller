# Description: Short example for Testing Time Series Stationarity with KPSS and Dickey Fuller.



from statsmodels.tsa.stattools import adfuller, kpss
import logging
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(42)

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)



# Stationary time series (white noise)
stationary_series = np.random.normal(loc=0, scale=1, size=500)
# Non-stationary time series (random walk)
non_stationary_series = np.cumsum(np.random.normal(loc=0, scale=1, size=500))
# Create a DataFrame for convenience
data = pd.DataFrame({
    "Stationary": stationary_series,
    "Non-Stationary": non_stationary_series
})

plt.figure(figsize=(12, 6))
plt.plot(data['Stationary'], label='Stationary Series')
plt.plot(data['Non-Stationary'], label='Non-Stationary Series')
plt.title('Stationary vs Non-Stationary Time Series')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.savefig('stationary_vs_non_stationary.png')
plt.show()

def kpss_test(series):
    statistic, p_value, _, critical_values = kpss(series, regression='c')
    logger.info("KPSS Test:")
    logger.info(f"Statistic: {statistic:.4f}")
    logger.info(f"P-Value: {p_value:.4f}")
    logger.info("Critical Values:")
    for key, value in critical_values.items():
        logger.info(f"{key}: {value:.4f}")
    logger.info(f"Conclusion: {'Stationary' if p_value > 0.05 else 'Non-Stationary'}\n")

def adf_test(series):
    statistic, p_value, _, _, critical_values, _ = adfuller(series)
    logger.info("Dickey-Fuller Test:")
    logger.info(f"Statistic: {statistic:.4f}")
    logger.info(f"P-Value: {p_value:.4f}")
    logger.info("Critical Values:")
    for key, value in critical_values.items():
        logger.info(f"{key}: {value:.4f}")
    logger.info(f"Conclusion: {'Stationary' if p_value < 0.05 else 'Non-Stationary'}\n")


logger.info("Testing the Stationary Series:\n")
kpss_test(data['Stationary'])
adf_test(data['Stationary'])

logger.info("Testing the Non-Stationary Series:\n")
kpss_test(data['Non-Stationary'])
adf_test(data['Non-Stationary'])
