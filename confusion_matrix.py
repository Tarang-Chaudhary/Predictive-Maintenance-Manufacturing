import matplotlib.pyplot as plt
import classification_model
import normalize_split
from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix

rf_clf  = classification_model.classifiers['Random Forest']
preds_r = rf_clf.predict(normalize_split.X_val_s)
cm      = confusion_matrix(normalize_split.y_val_c, preds_r)

disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                               display_labels=['Healthy', 'Near Failure'])
disp.plot(cmap='Blues')
plt.title('Confusion Matrix — Random Forest Classifier')
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=150)
plt.show()