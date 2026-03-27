from statsmodels.tsa.arima.model import ARIMA
import adf_test
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
# Train-test split on time series (80/20 by cycle)
n        = len(adf_test.sensor_series)
train_ts =adf_test.sensor_series[:int(n * 0.8)]
test_ts  = adf_test.sensor_series[int(n * 0.8):]

# Fit ARIMA(2, 1, 1): AR order=2, differencing=1, MA order=1
arima_model = ARIMA(train_ts, order=(2, 1, 1))
arima_fit   = arima_model.fit()
print(arima_fit.summary())

# Forecast
forecast = arima_fit.forecast(steps=len(test_ts))
rmse_arima = np.sqrt(mean_squared_error(test_ts, forecast))
print(f"\nARIMA Forecast RMSE: {rmse_arima:.4f}")

# Plot
plt.figure(figsize=(11, 5))
plt.plot(range(len(train_ts)),         train_ts, label='Training',   color='steelblue')
plt.plot(range(len(train_ts), n),      test_ts,  label='Actual',     color='green')
plt.plot(range(len(train_ts), n),      forecast, label='Forecast',   color='red', linestyle='--')
plt.axvline(len(train_ts), color='gray', linestyle=':', linewidth=1)
plt.title('ARIMA(2,1,1) — Sensor 2 Degradation Forecast')
plt.xlabel('Operational Cycle'); plt.ylabel('Sensor Value')
plt.legend(); plt.tight_layout()
plt.savefig('arima_forecast.png', dpi=150)
plt.show()