from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
import classification_model
import normalize_split
from sklearn.metrics import roc_auc_score
plt.figure(figsize=(8, 6))
for name, clf in classification_model.classifiers.items():
    if hasattr(clf, 'predict_proba'):
        probas = clf.predict_proba(normalize_split.X_val_s)[:, 1]
        fpr, tpr, _ = roc_curve(normalize_split.y_val_c, probas)
        auc = roc_auc_score(normalize_split.y_val_c, probas)
        plt.plot(fpr, tpr, linewidth=1.8, label=f'{name} (AUC={auc:.3f})')

plt.plot([0, 1], [0, 1], 'k--', linewidth=1)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate (Recall)')
plt.title('ROC Curves — Failure Classification Models')
plt.legend(loc='lower right', fontsize=9)
plt.tight_layout()
plt.savefig('roc_curves.png', dpi=150)
plt.show()