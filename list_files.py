"""
Date: November 21, 2022
Version: 1.1
Author: SangaeLama
Github: https://github.com/SangaeLama/Python-Google-Drive-API/blob/master/list_files.py
"""

from service_creator import Create_Service
from service_creator import Create_Service2
import pandas as pd

#--------------------------------------------------------------------------------------------
CLIENT_SECRET_FILE = 'client-secret.json'
SERVICE_ACCOUNT_FILE = 'service-account.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

driveID = '0AGRZ_Z8RC-_fUk9PVA'                             #drive ID of the shared drive.
folder_id = '1TZJzb9h8v5LhQB7WG9B2Im5toY1uQiHi'             #change this to choose the directory to upload the files to.
#----------------------------------------------------------------------------------------------------------------------------------

#service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
service = Create_Service2(SERVICE_ACCOUNT_FILE, API_NAME, API_VERSION, SCOPES)

query = f"parents = '{folder_id}'"

#response = service.files().list(q=query).execute()
response = service.files().list(q=query, includeItemsFromAllDrives=True, corpora='drive', driveId=driveID, supportsAllDrives=True).execute()
#print(response)
files = response.get('files')
#print(files)
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query, includeItemsFromAllDrives=True, corpora='drive', driveId=driveID, supportsAllDrives=True).execute()
    files.extend(response.get('files'))
    nextPageToken = response.get('nextPageToken')

dataFrame = pd.DataFrame(files)
print (dataFrame)
