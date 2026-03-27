import remove_constant
window = 30
train_df = remove_constant.train_df.sort_values(['unit_id', 'time_cycles'])

for sensor in remove_constant.selected_sensors:
    grp = train_df.groupby('unit_id')[sensor]
    train_df[f'{sensor}_rmean'] = grp.transform(
        lambda x: x.rolling(window, min_periods=1).mean())
    train_df[f'{sensor}_rstd']  = grp.transform(
        lambda x: x.rolling(window, min_periods=1).std().fillna(0))
    train_df[f'{sensor}_lag1']  = grp.shift(1).fillna(method='bfill')

# Clip RUL at 125 (piecewise linear — standard in PdM literature)
train_df['RUL_clipped'] = train_df['RUL'].clip(upper=125)

print(f"Total features: {train_df.shape[1]}")