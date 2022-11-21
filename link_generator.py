"""
Date: November 21, 2022
Version: 1.1
Author: SangaeLama
Github: https://github.com/SangaeLama/Python-Google-Drive-API/blob/master/link_generator.py
"""


from google_auth_oauthlib.flow import Flow, InstalledAppFlow

from service_creator import Create_Service

#--------------------------------------------------------------------------------------------
CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
#--------------------------------------------------------------------------------------------

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def sharer(ID):
    #share-link code starts here.
    file_id = ID

    #setting the permission attributes
    request_body = {
        'role': 'reader',
        'type': 'anyone'
        }
    response_permission = service.permissions().create(fileId=file_id, body=request_body, supportsAllDrives=True).execute()
    #print(response_permission)

    #Print Sharing Link
    response_share_link = service.files().get(
        fileId=file_id,
        fields='webViewLink',
        supportsAllDrives=True).execute()
    #print("The share link is : ")
    #print(response_share_link)
    print("\nGenerating the URL... OK!")
    #getting just the link from the object response_share_link
    link = response_share_link.get("webViewLink")
    return link

if __name__ == '__main__':
    file_id = '1mP1yT1PKf1-KxC9knQo4y-AXVe5M3OAe'               #change this to generate link for a different file

    link = sharer(file_id)

    print(link)

