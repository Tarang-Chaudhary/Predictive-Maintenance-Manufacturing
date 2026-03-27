from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibratedClassifierCV
import matplotlib.pyplot as plt
import pandas as pd
import normalize_split
lr_base = LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42)
calibrated_lr = CalibratedClassifierCV(lr_base, cv=5, method='isotonic')
calibrated_lr.fit(normalize_split.X_train_s, normalize_split.y_train_c)

# Propensity scores = probability of failure within 30 cycles
val_propensity = calibrated_lr.predict_proba(normalize_split.X_val_s)[:, 1]

# Segment into risk tiers
def risk_tier(p):
    if p < 0.30:   return 'Low'
    elif p < 0.65: return 'Medium'
    else:          return 'High'

risk_labels = pd.Series(val_propensity).apply(risk_tier)
print("Risk Tier Distribution:\n", risk_labels.value_counts())

# Plot propensity score distribution
plt.figure(figsize=(8, 4))
plt.hist(val_propensity, bins=40, color='steelblue', edgecolor='white')
plt.axvline(0.30, color='orange', linestyle='--', label='Low/Medium threshold')
plt.axvline(0.65, color='red',    linestyle='--', label='Medium/High threshold')
plt.title('Propensity Score Distribution — Failure Risk')
plt.xlabel('Predicted Probability of Failure (within 30 cycles)')
plt.ylabel('Count')
plt.legend(); plt.tight_layout()
plt.savefig('propensity_dist.png', dpi=150)
plt.show()