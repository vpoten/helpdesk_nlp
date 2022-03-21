import os
import pandas as pd


def load_dataset(path: str = None):
    if path is None:
        path = 'downloads/dataset.csv'

    return pd.read_csv(path)


def filter_dataset(df):
    df = df[(df['language'] == 'en') & (df['text'] != '') & (df['c1'] != '')]
    return df


if __name__ == "__main__":
    """
    This script loads the dataset and generates a clean version by applying some filters:
    (english, not null class, not null text)
    """
    df1 = load_dataset()
    print(df1.shape)
    df2 = filter_dataset(df1)
    print(df2.shape)
    base_path = 'downloads'
    df2.to_csv(os.path.join(base_path, 'dataset_clean.csv'),
               columns=['id', 'status', 'group', 'language', 'text', 'c1', 'c2', 'c3'])
    pass
