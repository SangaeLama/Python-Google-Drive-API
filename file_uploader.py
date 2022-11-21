import sys
import pandas as pd

from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request

from service_creator import Create_Service
from service_creator import Create_Service2
from link_generator import sharer
from sheet_writer import writer

#--------------------------------------------------------------------------------------------
CLIENT_SECRET_FILE = 'client-secret.json'
SERVICE_ACCOUNT_FILE = 'service-account.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
#--------------------------------------------------------------------------------------------

def uploader(service):
    #Upload code begins here.
    driveID = '0AGRZ_Z8RC-_fUk9PVA'
    file = sys.argv[1]
    folder_id = '1TZJzb9h8v5LhQB7WG9B2Im5toY1uQiHi'             #This is the folder_id where the files will be uploadeds

    #getting the folder name from the folder_id
    folder=service.files().get(fileId=folder_id, fields="name", supportsAllDrives=True).execute()
    folder_name=folder.get('name')
    print(f"Folder name : {folder_name}")

    # Upload the file
    file_metadata = {
        'name': file,
        #'parents': ['1PnEfdMLPxLynwZscq3rtmwePWHm23rnM']
        'parents' : [folder_id]        #change this to choose the directory to upload the files to.
    }

    media_content = MediaFileUpload(file, mimetype='image/png')

    #creating a query to see if the file is already uploaded
    query = (f"parents ={folder_id}") and (f"name contains '{file}'") #querying for a duplicate file

    response = service.files().list(q=query,includeItemsFromAllDrives=True, corpora='drive',driveId=driveID, supportsAllDrives=True).execute()
    files = response.get('files')

    #creating a dataframe out of the response received from query
    df = pd.DataFrame(files)
    #print(df)

    if df.empty:
        file = service.files().create(
            body=file_metadata,
            media_body=media_content,
            supportsAllDrives=True
        ).execute()

        fileName = file.get('name')
        print(f"\nFile {fileName} upload to drive... Successful!")

        ID = file.get("id")         #getting the ID of the file
        return ID
    else:
        print(f"\nFound some duplicates in : \'{folder_name}\' folder.")
        print(f"\n{df}")
        action = 'Y'
        action = input("\nDo you still want to upload the file? (Y/n)")
        if action == 'Y':
            file = service.files().create(
            body=file_metadata,
            media_body=media_content,
            supportsAllDrives=True
            ).execute()

            fileName = file.get('name')
            print("File "+fileName+ " upload to drive... Successful!")

            ID = file.get("id")         #getting the ID of the file
            return ID
        else:
            print("Quitting...")


if __name__ == '__main__':
    #creating a service from the client-secret.json file
    #service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    #creating a service from the service-account.json file
    service = Create_Service2(SERVICE_ACCOUNT_FILE, API_NAME, API_VERSION, SCOPES)
    ID=uploader(service)
    if ID:
        link = sharer(ID)
        SPREADSHEET_ID= '1YhRNHUeIIrYKljx2774XFluy54VorBIcZnfbmXyVIm4'
        writer(SPREADSHEET_ID, sys.argv[1], ID, link)
