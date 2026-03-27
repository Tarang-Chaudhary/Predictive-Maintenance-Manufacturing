from sklearn.ensemble import RandomForestClassifier
import normalize_split
# Balanced weights (auto-computed by sklearn)
rf_bal = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
rf_bal.fit(normalize_split.X_train_s,normalize_split. y_train_c)

# Custom weights: missing a failure costs 10x more than a false alarm
rf_cost = RandomForestClassifier(n_estimators=100, class_weight={0: 1, 1: 10}, random_state=42)
rf_cost.fit(normalize_split.X_train_s,normalize_split. y_train_c)