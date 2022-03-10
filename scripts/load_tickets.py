import os
import os.path
import json
import time

from requests.exceptions import RequestException

from src.freshdesk.api_client import ApiClient
import src.freshdesk.export_loader as export
from config.config import API_TOKEN


def _filename(out_path, ticket_id):
    return os.path.join(out_path, f'{str(ticket_id)}.json')


def save_conversation(out_path, ticket_id, data):
    with open(_filename(out_path, ticket_id), "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    """
    Load tickets
    """

    client = ApiClient('doofinder', API_TOKEN)

    # load tickets inventory
    df = export.load_export()
    ticket_ids = export.get_ticket_ids(df)

    # create download directory
    out_path = 'downloads/tickets'
    os.makedirs(out_path, exist_ok=True)

    for ticket_id in ticket_ids:
        if os.path.exists(_filename(out_path, ticket_id)):
            continue
        try:
            data = client.get_ticket(ticket_id)
        except RequestException as err:
            print(f'Error downloading data for ticket [{ticket_id}]: {str(err)}')
        else:
            save_conversation(out_path, ticket_id, data)
            time.sleep(0.05)  # sleep to not exceed the rate limit
