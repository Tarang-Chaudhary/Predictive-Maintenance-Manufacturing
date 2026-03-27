import matplotlib.pyplot as plt
import seaborn as sns
import rolling_window
import remove_constant
corr = rolling_window.train_df[remove_constant.selected_sensors].corr()
plt.figure(figsize=(12, 9))
sns.heatmap(corr, annot=False, cmap='coolwarm', center=0, linewidths=0.3)
plt.title('Sensor Correlation Heatmap')
plt.tight_layout()
plt.savefig('sensor_correlation.png', dpi=150)
plt.show()