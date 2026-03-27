from statsmodels.tsa.ar_model import AutoReg
import adf_test
import matplotlib.pyplot as plt

# Fit AR(2) based on PACF analysis
ar_model = AutoReg(adf_test.sensor_diff, lags=2, old_names=False)
ar_fit   = ar_model.fit()
print(ar_fit.summary())

# In-sample fitted values
fitted_vals = ar_fit.fittedvalues

plt.figure(figsize=(10, 4))
plt.plot(adf_test.sensor_diff,  label='Actual (differenced)', color='steelblue', linewidth=0.9)
plt.plot(fitted_vals,  label='AR(2) Fitted',          color='red',       linewidth=0.9, linestyle='--')
plt.title('AR(2) Model Fit — Sensor 2')
plt.xlabel('Cycle'); plt.ylabel('Differenced Value')
plt.legend(); plt.tight_layout()
plt.savefig('ar_model_fit.png', dpi=150)
plt.show()