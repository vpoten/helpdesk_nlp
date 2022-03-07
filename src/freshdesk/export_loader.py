import pandas
import pandas as pd


def load_export(path: str = None):
    if path is None:
        path = 'data/export_20210901_20220307.csv.gz'

    df = pd.read_csv(path)
    return df


def get_ticket_ids(df: pandas.DataFrame):
    return df['Ticket ID'].to_list()


def filter_by(df: pandas.DataFrame, status: list = None, group: list = None):
    if status:
        df = df[df['Status'].isin(status)]
    if group:
        df = df[df['Group'].isin(group)]
    return df
