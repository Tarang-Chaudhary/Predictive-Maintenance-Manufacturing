import pandas as pd
import numpy as np

# CMAPSS has no header — assign column names manually
cols = ['unit_id', 'time_cycles', 'op_1', 'op_2', 'op_3'] + \
       [f'sensor_{i}' for i in range(1, 22)]

train_df = pd.read_csv('train_FD001.txt', sep='\s+', header=None, names=cols)
test_df  = pd.read_csv('test_FD001.txt',  sep='\s+', header=None, names=cols)
rul_df   = pd.read_csv('RUL_FD001.txt',   header=None, names=['RUL'])

# Compute RUL: max_cycle_per_engine - current_cycle
max_cycles = train_df.groupby('unit_id')['time_cycles'].max().reset_index()
max_cycles.columns = ['unit_id', 'max_cycles']
train_df = train_df.merge(max_cycles, on='unit_id')
train_df['RUL'] = train_df['max_cycles'] - train_df['time_cycles']

print(train_df.shape)
print(train_df.head())
print(train_df.describe())