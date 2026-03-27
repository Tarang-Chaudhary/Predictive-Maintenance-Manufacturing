from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import normalize_split
import numpy as np
import pandas as pd
reg_models = {
    'Linear Regression'  : LinearRegression(),
    'Ridge (alpha=10)'   : Ridge(alpha=10),
    'Lasso (alpha=0.1)'  : Lasso(alpha=0.1, max_iter=5000),
    'Random Forest'      : RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1),
    'Gradient Boosting'  : GradientBoostingRegressor(n_estimators=200, learning_rate=0.05,
                                                      max_depth=5, random_state=42),
}

reg_results = {}
for name, model in reg_models.items():
    model.fit(normalize_split.X_train_s,normalize_split.y_train_r)
    preds = model.predict(normalize_split.X_val_s)
    rmse  = np.sqrt(mean_squared_error(normalize_split.y_val_r, preds))
    mae   = mean_absolute_error(normalize_split.y_val_r, preds)
    r2    = r2_score(normalize_split.y_val_r, preds)
    reg_results[name] = {'RMSE': round(rmse, 2), 'MAE': round(mae, 2), 'R2': round(r2, 3)}
    print(f"{name:25s} | RMSE: {rmse:.2f} | MAE: {mae:.2f} | R2: {r2:.3f}")

results_df = pd.DataFrame(reg_results).T
print("\n", results_df)