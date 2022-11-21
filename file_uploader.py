"""
Date: November 21, 2022
Version: 2.3
Author: SangaeLama
Github: https://github.com/SangaeLama/Python-Google-Drive-API/blob/master/file_uploader.py
"""
import sys
import pandas as pd

from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request

from service_creator import Create_Service
from service_creator import Create_Service2
from link_generator import sharer
from sheet_writer import writer

#----------------------------------------------------------------------------------------------------------------------------------
CLIENT_SECRET_FILE = 'client-secret.json'
SERVICE_ACCOUNT_FILE = 'service-account.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
#----------------------------------------------------------------------------------------------------------------------------------
#Google spreadsheet to write data on, note that the sheet must have write access to the service account.
SPREADSHEET_ID= '1YhRNHUeIIrYKljx2774XFluy54VorBIcZnfbmXyVIm4'
MIME_TYPE = 'image/png'                                     #change this according to the type of file being uploaded.
driveID = '0AGRZ_Z8RC-_fUk9PVA'                             #drive ID of the shared drive.
folder_id = '1TZJzb9h8v5LhQB7WG9B2Im5toY1uQiHi'             #change this to choose the directory to upload the files to.
#----------------------------------------------------------------------------------------------------------------------------------

def uploader(service):

    #destination folder information
    folder=service.files().get(fileId=folder_id, fields="name", supportsAllDrives=True).execute()
    folder_name=folder.get('name')
    print(f"\nDestination folder : \"{folder_name}\"")

    # defining the file to upload
    file = sys.argv[1]
    file_metadata = {
        'name': file,
        'parents' : [folder_id]                             #This is the folder_id where the files will be uploaded
    }
    media_content = MediaFileUpload(file)#, mimetype=MIME_TYPE)

    #creating a query to see if the file is already uploaded
    query = (f"parents ={folder_id}") and (f"name contains '{file}'") #querying for a duplicate file

    print("\nScanning the destination folder for duplicate files...")
    #applying the query to search for files in the shared drive
    response = service.files().list(q=query,includeItemsFromAllDrives=True, corpora='drive',driveId=driveID, supportsAllDrives=True).execute()

    files = response.get('files')

    #creating a dataframe out of the response received from query
    df = pd.DataFrame(files)
    #print(df)

    if df.empty:
        print("\nUploading the file...")
        file = service.files().create(
            body=file_metadata,
            media_body=media_content,
            supportsAllDrives=True
        ).execute()

        fileName = file.get('name')
        print(f"\n \"{fileName}\" upload to drive... Successful!")

        ID = file.get("id")         #getting the ID of the file
        return ID
    else:
        print(f"\nFound some duplicates in : \"{folder_name}\" folder.")
        print(f"\n{df}")

        action = input("\nDo you still want to upload the file? (y/N)")
        if action == 'Y'or 'y':
            print("\nUploading the file...")
            file = service.files().create(
            body=file_metadata,
            media_body=media_content,
            supportsAllDrives=True
            ).execute()

            fileName = file.get('name')
            print(f"\n \"{fileName}\" upload to drive... Successful!")

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
        writer(SPREADSHEET_ID, sys.argv[1], ID, link)
    print("\n\t\t...THE END...")
