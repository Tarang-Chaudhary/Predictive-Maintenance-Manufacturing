from statsmodels.tsa.stattools import adfuller
import pandas as pd
import visualize_sensor
sensor_series = visualize_sensor.engine_1['sensor_2'].values

def adf_test(series, name='Series'):
    result = adfuller(series)
    print(f"\n--- ADF Test: {name} ---")
    print(f"  ADF Statistic : {result[0]:.4f}")
    print(f"  p-value       : {result[1]:.4f}")
    print(f"  Stationary?   : {'YES' if result[1] < 0.05 else 'NO — needs differencing'}")
    return result[1] < 0.05

is_stationary = adf_test(sensor_series, 'Sensor 2 (raw)')

if not is_stationary:
    sensor_diff = pd.Series(sensor_series).diff().dropna().values
    adf_test(sensor_diff, 'Sensor 2 (1st difference)')
else:
    sensor_diff = sensor_series