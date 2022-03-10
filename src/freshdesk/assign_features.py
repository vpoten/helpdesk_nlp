import export_loader as export_loader
from src.nlp.language_detector import detect_language

ID = export_loader.ID
GROUP = export_loader.GROUP
STATUS = export_loader.STATUS


def get_class1(group):
    # TODO
    return None


def get_class2(group):
    # TODO
    return None


def get_class3(group):
    # TODO
    return None


def get_language(conversation):
    text = None if not conversation else conversation[0].get('body_text', None)
    return None if not text else detect_language(text)


def get_clean_text(conversation):
    # TODO
    return None


def _build_features(ticket_id, row):
    group = row[GROUP]
    status = row[STATUS]
    conversation = export_loader.load_conversation(ticket_id)
    language = get_language(conversation)
    text = get_clean_text(conversation)
    c1 = get_class1(group)
    c2 = get_class2(group)
    c3 = get_class3(group)
    return {
        'id': ticket_id,
        'status': status,
        'language': language,
        'text': text,
        'c1': c1,
        'c2': c2,
        'c3': c3,
    }


def assign_features():
    df = export_loader.load_export()
    ticket_ids = df[ID]
    ticket_features = []

    for ticket_id in ticket_ids:
        row = df.loc[df[ID] == ticket_id]
        features = _build_features(ticket_id, row)
        ticket_features.append(features)

    return ticket_features


if __name__ == "__main__":
    c = export_loader.load_conversation('56929')
    print(c)
    fl = assign_features()
    print(fl[0])