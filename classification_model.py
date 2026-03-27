from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
import normalize_split
classifiers = {
    'Logistic Regression' : LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42),
    'LDA'                 : LinearDiscriminantAnalysis(),
    'Decision Tree'       : DecisionTreeClassifier(max_depth=6, class_weight='balanced', random_state=42),
    'Random Forest'       : RandomForestClassifier(n_estimators=100, class_weight='balanced',
                                                   random_state=42, n_jobs=-1),
    'SVM (RBF)'           : SVC(kernel='rbf', class_weight='balanced', probability=True, random_state=42),
}

for name, clf in classifiers.items():
    clf.fit(normalize_split.X_train_s, normalize_split.y_train_c)
    preds  = clf.predict(normalize_split.X_val_s)
    probas = clf.predict_proba(normalize_split.X_val_s)[:, 1] if hasattr(clf, 'predict_proba') else None
    auc    = roc_auc_score(normalize_split.y_val_c, probas) if probas is not None else 'N/A'
    print(f"\n{'='*45}")
    print(f"  {name}")
    print(f"{'='*45}")
    print(classification_report(normalize_split.y_val_c, preds, target_names=['Healthy', 'Near Failure']))
    print(f"  ROC-AUC: {auc:.4f}" if isinstance(auc, float) else f"  ROC-AUC: {auc}")