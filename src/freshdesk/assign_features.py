import os.path
import pandas as pd

import export_loader as export_loader
import src.definitions.group_class as group_class
from src.nlp.language_detector import detect_language

ID = export_loader.ID
GROUP = export_loader.GROUP
STATUS = export_loader.STATUS


def get_class1(group):
    return group_class.CLASS_L1.get(group)


def get_class2(group):
    return group_class.CLASS_L2.get(group)


def get_class3(group):
    return group_class.CLASS_L3.get(group)


def get_language(text):
    try:
        return None if not text else detect_language(text)
    except Exception as err:
        return None


def get_message_text(message):
    return None if not message else message.get('description_text')


def _build_features(ticket_id, row):
    group = row.iloc[0][GROUP]
    status = row.iloc[0][STATUS]
    message = export_loader.load_ticket(ticket_id)
    text = get_message_text(message)
    language = get_language(text)
    c1 = get_class1(group)
    c2 = get_class2(group)
    c3 = get_class3(group)
    return {
        'id': ticket_id,
        'status': status,
        'group': group,
        'language': language,
        'text': text,
        'c1': c1,
        'c2': c2,
        'c3': c3,
    }


def build_patterns() -> list:
    df = export_loader.load_export()
    ticket_ids = df[ID]
    ticket_features = []

    for ticket_id in ticket_ids:
        row = df.loc[df[ID] == ticket_id]
        features = _build_features(ticket_id, row)
        ticket_features.append(features)

    return ticket_features


def save_patterns(patterns: list, base_path: str = None):
    df = pd.DataFrame(patterns)
    base_path = 'downloads' if base_path is None else base_path
    df.to_csv(os.path.join(base_path, 'dataset.csv'))


if __name__ == "__main__":
    c = export_loader.load_conversation('56929')
    print(c)
    patterns = build_patterns()
    print(patterns[0])
    save_patterns(patterns)
