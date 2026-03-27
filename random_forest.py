import regression_models
import pandas as pd
import matplotlib.pyplot as plt
import normalize_split
rf_model = regression_models.reg_models['Random Forest']
importances = pd.Series(rf_model.feature_importances_, index=normalize_split.feature_cols)
top20 = importances.nlargest(20).sort_values()

plt.figure(figsize=(9, 7))
top20.plot(kind='barh', color='steelblue', edgecolor='white')
plt.title('Top 20 Feature Importances — Random Forest RUL Prediction')
plt.xlabel('Importance Score')
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=150)
plt.show()