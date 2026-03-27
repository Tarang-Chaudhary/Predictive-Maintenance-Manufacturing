import load_dataset
import matplotlib.pyplot as plt

engine_1 = load_dataset.train_df[load_dataset.train_df['unit_id'] == 1].sort_values('time_cycles')

key_sensors = ['sensor_2', 'sensor_3', 'sensor_4', 'sensor_7',
               'sensor_8', 'sensor_11', 'sensor_12', 'sensor_13', 'sensor_15']

fig, axes = plt.subplots(3, 3, figsize=(14, 9))
for ax, sensor in zip(axes.flatten(), key_sensors):
    ax.plot(engine_1['time_cycles'], engine_1[sensor],
            color='steelblue', linewidth=0.9)
    ax.set_title(sensor, fontsize=10)
    ax.set_xlabel('Cycle', fontsize=8)
    ax.set_ylabel('Value', fontsize=8)

plt.suptitle('Sensor Degradation Trends — Engine Unit 1', fontsize=13)
plt.tight_layout()
plt.savefig('sensor_trends.png', dpi=150)
plt.show()