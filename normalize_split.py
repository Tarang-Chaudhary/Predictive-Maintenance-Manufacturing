from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import rolling_window
feature_cols = [c for c in rolling_window.train_df.columns
                if c not in ['unit_id', 'time_cycles', 'RUL', 'RUL_clipped', 'max_cycles']]

X      = rolling_window.train_df[feature_cols]
y_reg  =rolling_window. train_df['RUL_clipped']               # Regression target
y_cls  = (rolling_window.train_df['RUL'] <= 30).astype(int)  # Classification target

X_train, X_val, y_train_r, y_val_r = train_test_split(
    X, y_reg, test_size=0.2, random_state=42)
_, _, y_train_c, y_val_c = train_test_split(
    X, y_cls, test_size=0.2, random_state=42)

scaler    = MinMaxScaler()
X_train_s = scaler.fit_transform(X_train)
X_val_s   = scaler.transform(X_val)

print("Class distribution (train):", y_train_c.value_counts().to_dict())