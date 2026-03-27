import class_custom
import normalize_split
# Default threshold = 0.5 — but we can lower it to catch more failures
probas_bal = class_custom.rf_bal.predict_proba(normalize_split.X_val_s)[:, 1]

thresholds = [0.3, 0.4, 0.5, 0.6]
print(f"\n{'Threshold':>12} | {'Recall(Fail)':>13} | {'Precision(Fail)':>16} | {'F1(Fail)':>10}")
print("-" * 58)

from sklearn.metrics import precision_score, recall_score, f1_score
for thresh in thresholds:
    preds_t   = (probas_bal >= thresh).astype(int)
    recall_f  = recall_score(normalize_split.y_val_c, preds_t)
    precision_f = precision_score(normalize_split.y_val_c, preds_t, zero_division=0)
    f1_f      = f1_score(normalize_split.y_val_c, preds_t, zero_division=0)
    print(f"{thresh:>12.1f} | {recall_f:>13.3f} | {precision_f:>16.3f} | {f1_f:>10.3f}")