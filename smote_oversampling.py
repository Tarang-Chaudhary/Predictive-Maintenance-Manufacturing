# pip install imbalanced-learn
from imblearn.over_sampling import SMOTE
from imblearn.combine import SMOTETomek
import normalize_split
import pandas as pd
smote = SMOTE(random_state=42, k_neighbors=5)
X_sm, y_sm = smote.fit_resample(normalize_split.X_train_s, normalize_split.y_train_c)
print("After SMOTE:", pd.Series(y_sm).value_counts().to_dict())

smotetomek = SMOTETomek(random_state=42)
X_st, y_st = smotetomek.fit_resample(normalize_split.X_train_s, normalize_split.y_train_c)
print("After SMOTETomek:", pd.Series(y_st).value_counts().to_dict())