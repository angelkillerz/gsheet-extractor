import httplib2
import os

from apiclient import discovery
from google.oauth2 import service_account

try:
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    secret_file = os.path.join(os.getcwd(), 'client_secret.json')

    spreadsheet_id = "xxx"
    data_range = "Sheet2!A3:F7" 


except OSError as e:

    print e


