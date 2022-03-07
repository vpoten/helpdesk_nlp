import os
import os.path
import json
import time

from requests.exceptions import RequestException

from src.freshdesk.api_client import ApiClient
import src.freshdesk.export_loader as export
from config.config import API_TOKEN


def save_conversation(out_path, ticket_id, data):
    filename = os.path.join(out_path, f'{str(ticket_id)}.json')
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    """
    Load ticket conversations
    """

    client = ApiClient('doofinder', API_TOKEN)

    # load tickets inventory
    df = export.load_export()
    ticket_ids = export.get_ticket_ids(df)

    # create download directory
    out_path = 'downloads/conversations'
    os.makedirs(out_path)

    for ticket_id in ticket_ids:
        try:
            data = client.get_ticket_conversations(ticket_id)
        except RequestException as err:
            print(f'Error downloading data for ticket [{ticket_id}]: {str(err)}')
        else:
            save_conversation(out_path, ticket_id, data)
            time.sleep(0.001)
