from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
import pandas as pd
import adf_test
fig, axes = plt.subplots(1, 2, figsize=(13, 4))
plot_acf( pd.Series(adf_test.sensor_diff), lags=40, ax=axes[0],
          title='ACF — Sensor 2 (after differencing)')
plot_pacf(pd.Series(adf_test.sensor_diff), lags=40, ax=axes[1],
          title='PACF — Sensor 2 (after differencing)')
plt.tight_layout()
plt.savefig('acf_pacf.png', dpi=150)
plt.show()
# Read PACF: where it drops within bounds = AR order p