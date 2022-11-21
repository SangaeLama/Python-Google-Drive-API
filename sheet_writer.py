import sys
from googleapiclient.discovery import build         #for building service
from google.oauth2 import service_account           #to work with service service_account

SERVICE_ACCOUNT_FILE = 'service-account.json'         #downloaded from console and stored in the working discovery
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def writer(SPREADSHEET_ID, file_name, file_id, link):

    #building the service
    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()      #just making it short

    #--------------writing values to the cells of Sheet2
    value = [[file_name,file_id, link]]

    #write data valB into the cells starting from B1 of Sheet2
    #request = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range = "Sheet2!B1", valueInputOption = "RAW", body={"values":valB}).execute()

    #requestA = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range = "Sheet2!A1:B", valueInputOption = "RAW", body={"values":vals}).execute()

    requestB = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range = "Sheet2!A1:C", valueInputOption = "RAW", body={"values":value}).execute()

    print("\nFilling up the google sheet... OK!")

#if __name__ == '__main__':
#    SPREADSHEET_ID= '1YhRNHUeIIrYKljx2774XFluy54VorBIcZnfbmXyVIm4'
#    writer(SPREADSHEET_ID, 'hari.png', 'thisIsTheFileID', 'thisIsTheShareLink')
