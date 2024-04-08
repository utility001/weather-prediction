import pandas as pd

def get_prepared_data(set):
    """
    Returns a DataFrame containg train or test set based on what you specify

    set : 'train' for train set. 'test' for test set
    """

    if set == 'train':
        df = pd.read_csv('data/DailyDelhiClimateTrain.csv', index_col='date', parse_dates=True)
        df = df.drop(index=["2017-01-01"])
        assert df.shape == (1461, 4), "Did you change the train set. If you did, then you need to modify this wrangle function"
    elif set == 'test':
        df = pd.read_csv('data/DailyDelhiClimateTest.csv', index_col='date', parse_dates=True)

    # Create new columns
    df.index.freq = 'D'
    df["year"] = df.index.year
    df["month"] = df.index.month
    df["day_of_month"] = df.index.day
    df["weekday"] = df.index.weekday
    df['quarter'] = df.index.quarter
    df["day_of_year"] = df.index.dayofyear

    return df