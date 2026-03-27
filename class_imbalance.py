import normalize_split
import matplotlib.pyplot as plt
print("Class Distribution (Training):")
print(normalize_split.y_train_c.value_counts())
print(f"\nImbalance Ratio: {normalize_split.y_train_c.value_counts()[0] / normalize_split.y_train_c.value_counts()[1]:.1f}:1")

# Visualize
normalize_split.y_train_c.value_counts().plot(
    kind='bar', color=['steelblue', 'crimson'], edgecolor='white', figsize=(6, 4))
plt.title('Class Distribution — Failure Labels')
plt.xticks([0, 1], ['Healthy (0)', 'Near Failure (1)'], rotation=0)
plt.ylabel('Sample Count')
plt.tight_layout()
plt.savefig('class_distribution.png', dpi=150)
plt.show()