from service_creator import Create_Service
import pandas as pd

#--------------------------------------------------------------------------------------------
CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
#--------------------------------------------------------------------------------------------

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1PnEfdMLPxLynwZscq3rtmwePWHm23rnM'             #This is the apitest folder_id

query = f"parents = '{folder_id}'"

response = service.files().list(q=query).execute()
#print(response)
files = response.get('files')
#print(files)
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query).execute()
    files.extend(response.get('files'))
    nextPageToken = response.get('nextPageToken')

dataFrame = pd.DataFrame(files)
print (dataFrame)
