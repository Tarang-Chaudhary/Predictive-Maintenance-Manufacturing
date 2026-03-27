from sklearn.feature_selection import VarianceThreshold
import load_dataset
sensor_cols = [f'sensor_{i}' for i in range(1, 22)]

selector = VarianceThreshold(threshold=0.01)
selector.fit(load_dataset.train_df[sensor_cols])

selected_sensors = [c for c, keep in zip(sensor_cols, selector.get_support()) if keep]
dropped_sensors  = [c for c, keep in zip(sensor_cols, selector.get_support()) if not keep]

print("Dropped (constant):", dropped_sensors)
# Typically: sensor_1, sensor_5, sensor_6, sensor_10, sensor_16, sensor_18, sensor_19

train_df = load_dataset.train_df[['unit_id', 'time_cycles', 'RUL'] + selected_sensors]