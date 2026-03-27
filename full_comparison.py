from sklearn.metrics import f1_score, recall_score
from sklearn.ensemble import RandomForestClassifier
import normalize_split
import smote_oversampling
from sklearn.metrics import roc_auc_score
remedies = {
    'Baseline (no handling)'    : RandomForestClassifier(n_estimators=100, random_state=42),
    'class_weight=balanced'     : RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42),
    'SMOTE'                     : RandomForestClassifier(n_estimators=100, random_state=42),
    'SMOTETomek'                : RandomForestClassifier(n_estimators=100, random_state=42),
    'Custom weights (1:10)'     : RandomForestClassifier(n_estimators=100, class_weight={0:1, 1:10}, random_state=42),
}

train_data = {
    'Baseline (no handling)'    : (normalize_split.X_train_s,normalize_split. y_train_c),
    'class_weight=balanced'     : (normalize_split.X_train_s,normalize_split. y_train_c),
    'SMOTE'                     : (smote_oversampling.X_sm, smote_oversampling.y_sm),
    'SMOTETomek'                : (smote_oversampling.X_st, smote_oversampling.y_st),
    'Custom weights (1:10)'     : (normalize_split.X_train_s,normalize_split. y_train_c),
}

print(f"\n{'Method':30} | {'Recall(Fail)':>13} | {'F1(Fail)':>10} | {'AUC':>8}")
print("-" * 70)
for name, model in remedies.items():
    Xtr, ytr = train_data[name]
    model.fit(Xtr, ytr)
    preds  = model.predict(normalize_split.X_val_s)
    probas = model.predict_proba(normalize_split.X_val_s)[:, 1]
    print(f"{name:30} | {recall_score(normalize_split.y_val_c, preds):>13.3f} | "
          f"{f1_score(normalize_split.y_val_c, preds):>10.3f} | {roc_auc_score(normalize_split.y_val_c, probas):>8.3f}")