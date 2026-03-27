import matplotlib.pyplot as plt 
import regression_models
import normalize_split
gb_model = regression_models.reg_models['Gradient Boosting']
preds_gb  = gb_model.predict(normalize_split.X_val_s)

plt.figure(figsize=(7, 6))
plt.scatter(normalize_split.y_val_r, preds_gb, alpha=0.3, color='steelblue', s=10)
plt.plot([0, 125], [0, 125], 'r--', linewidth=1.5)
plt.title('Actual vs Predicted RUL — Gradient Boosting')
plt.xlabel('Actual RUL')
plt.ylabel('Predicted RUL')
plt.tight_layout()
plt.savefig('actual_vs_predicted.png', dpi=150)
plt.show()