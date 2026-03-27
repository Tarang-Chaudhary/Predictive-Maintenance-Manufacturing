from sklearn.model_selection import GridSearchCV, KFold
import normalize_split
from sklearn.ensemble import GradientBoostingRegressor

param_grid = {
    'n_estimators'  : [100, 200],
    'max_depth'     : [4, 5, 6],
    'learning_rate' : [0.05, 0.1],
    'subsample'     : [0.8, 1.0],
}
kf = KFold(n_splits=5, shuffle=True, random_state=42)
gb_search = GridSearchCV(
    GradientBoostingRegressor(random_state=42),
    param_grid, cv=kf,
    scoring='neg_root_mean_squared_error',
    n_jobs=-1, verbose=1
)
gb_search.fit(normalize_split.X_train_s, normalize_split.y_train_r)
print("Best Parameters:", gb_search.best_params_)
print("Best CV RMSE:   ", -gb_search.best_score_)