import requests


class ApiClient(object):
    """
    Basic freshdesk API client
    """

    def __init__(self, domain, token):
        self.domain = domain
        self.token = token
        self.session = requests.Session()
        # self.session.verify = False
        self.session.auth = (self.token, 'X')
        self.api_url = f'https://{self.domain}.freshdesk.com/api/v2'

    def get_ticket_conversations(self, ticket_id):
        endpoint = f'{self.api_url}/tickets/{str(ticket_id)}/conversations'
        r = self.session.get(endpoint)
        r.raise_for_status()
        return r.json()
