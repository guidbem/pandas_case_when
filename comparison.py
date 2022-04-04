import seaborn as sns
import pandas as pd
from utils import *


df = sns.load_dataset('taxis')

df.dtypes

df['pickup'] = pd.to_datetime(df['pickup'])
df['pickup_hour'] = df.pickup.dt.hour

for func in [if_elif_func, loc_mask, np_where]:
    print('Using {}:'.format(func.__name__))
    
    if func.__name__ == 'if_elif_func':
        %timeit -r10 df['fare_multiplier'] = df.apply(func, axis=1)
    else:
        %timeit -r10 df['fare_multiplier'] = func(df)

    df.drop(columns='fare_multiplier')

# Rules:

# If pickup is between 6am and 10pm:
#   1 passenger -> fare multiplier = 1.00
#   2 passengers -> fare multiplier = 1.05
#   3 passengers -> fare multiplier = 1.10
#   4 passengers -> fare multiplier = 1.15

# If pickup is between 10pm and 6am:
#   1 passenger -> fare multiplier = 1.20
#   2 passengers -> fare multiplier = 1.25
#   3 passengers -> fare multiplier = 1.30
#   4 passengers -> fare multiplier = 1.35

