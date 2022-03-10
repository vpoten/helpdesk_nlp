import os
import pandas as pd
import json

ID = 'Ticket ID'
GROUP = 'Group'
STATUS = 'Status'


def load_export(path: str = None):
    if path is None:
        path = 'data/export_20210901_20220307.csv.gz'

    df = pd.read_csv(path)
    return df


def get_ticket_ids(df: pd.DataFrame):
    return df[ID].to_list()


def filter_by(df: pd.DataFrame, status: list = None, group: list = None):
    if status:
        df = df[df['Status'].isin(status)]
    if group:
        df = df[df['Group'].isin(group)]
    return df


def load_conversation(ticket_id, base_path: str = None):
    base_path = 'downloads/conversations' if base_path is None else base_path
    with open(os.path.join(base_path, f'{str(ticket_id)}.json'), 'r') as fp:
        return json.load(fp)


def load_ticket(ticket_id, base_path: str = None):
    base_path = 'downloads/tickets' if base_path is None else base_path
    with open(os.path.join(base_path, f'{str(ticket_id)}.json'), 'r') as fp:
        return json.load(fp)
