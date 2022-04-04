import numpy as np

def if_elif_func(row):

    if (row['pickup_hour'] >= 6) & (row['pickup_hour'] < 22):
        if row['passengers'] == 1:
            return 1.00
        elif row['passengers'] == 2:
            return 1.05
        elif row['passengers'] == 3:
            return 1.10
        else:
            return 1.15

    else:
        if row['passengers'] == 1:
            return 1.20
        elif row['passengers'] == 2:
            return 1.25
        elif row['passengers'] == 3:
            return 1.30
        else:
            return 1.35

def loc_mask(df):

    df = df[['pickup_hour', 'passengers']].copy()

    df['fare_multiplier'] = 1.35

    df['fare_multiplier'] = df['fare_multiplier']\
        .mask(df['passengers'] == 3, 1.30)\
        .mask(df['passengers'] == 2, 1.25)\
        .mask(df['passengers'] == 1, 1.20)\
        .mask(((df['pickup_hour'] >= 6) & (df['pickup_hour'] < 22)), 1.15)\
        .mask((df['passengers'] == 3) & 
            ((df['pickup_hour'] >= 6) & (df['pickup_hour'] < 22)), 1.10)\
        .mask((df['passengers'] == 2) & 
            ((df['pickup_hour'] >= 6) & (df['pickup_hour'] < 22)), 1.05)\
        .mask((df['passengers'] == 1) & 
            ((df['pickup_hour'] >= 6) & (df['pickup_hour'] < 22)), 1.00)

    return df['fare_multiplier']

def np_where(df):

    df = df[['pickup_hour', 'passengers']].copy()

    df['fare_multiplier'] = np.where(
        (df['pickup_hour'] >= 6) & (df['pickup_hour'] < 22),

        np.where(df['passengers'] == 1, 1.00,
            np.where(df['passengers'] == 2, 1.05,
                np.where(df['passengers'] == 3, 1.10, 1.15)
                )
            ),

        np.where(df['passengers'] == 1, 1.20,
            np.where(df['passengers'] == 2, 1.25,
                np.where(df['passengers'] == 3, 1.30, 1.35)
                )
            )
    )

    return df['fare_multiplier']