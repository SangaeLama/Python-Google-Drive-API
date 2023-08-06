 # Python Google Drive API

This repository contains Python scripts for interacting with the Google Drive API. The scripts provide functionality to upload files, generate shareable links, list files, and write data to a Google Sheets spreadsheet. The Google Drive API is utilized to perform these tasks.

## Prerequisites

Before using the scripts in this repository, ensure you have the following:

- Python 3.x
- Required Python packages: `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, `google-api-python-client`, `pandas`, `jq` (for certain scripts)
- Google account with API access enabled
- Generated client secret JSON or service account JSON credentials
- Access to a Google Drive folder and Google Sheets spreadsheet for testing

On Google Cloud Console:
1. Enable the Drive API and Sheets API. 
    
2. Create an Oauth 2.0 Client ID and download&rename it as client-secret.json in the working directory


At Client Side:
1. Install python libraries at client side.
   ```
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib pandas pickle
   ```
2. Edit the python files to specify where the file should be uploaded by editing the folder_id, and driveID if working with Shared Drives.

## Scripts

### 1. file_uploader.py

This script allows you to upload files to a specific Google Drive folder. It provides options to handle duplicate files and scans the destination folder for duplicates before uploading.

Usage:
 ```bash
 python file_uploader.py <file_to_upload>
```

### 2. link_generator.py
Generates a shareable link for a specified file in Google Drive. This script is helpful when you want to create a shareable link to a file for sharing with others.

### 3. list_files.py
Lists all files in a specified Google Drive folder. It retrieves the list of files and displays them as a Pandas DataFrame for easy visualization

### 4. service_creator.py
Provides functions to create service objects for interacting with the Google Drive API. It supports both client secret and service account credentials.

### 5. sheet_writer.py
Writes data to a Google Sheets spreadsheet. It requires a Google Sheets ID and writes information about uploaded files to the spreadsheet.


## Getting Started
1. Clone this repository to your local machine.
2. Obtain the necessary credentials from the Google Developers Console.
3. Configure the appropriate credentials (client secret JSON or service account JSON) in the scripts.
4. Install required Python packages using `pip install -r requirements.txt`.
5. Run the desired script from the command line, following the usage instructions provided above.

## Notes
These scripts are intended for educational and personal use. Be cautious when handling sensitive data or using API credentials.

Ensure that you comply with Google's terms of use and API usage policies.

Adjust the scripts as needed to suit your specific requirements.

## Acknowledgments
The scripts in this repository utilize the Google Drive API to provide file management and sharing capabilities. Credits to Google for providing this API.

Version: : `1.1`
Added support of service accounts instead of just Oauth2.0 tokens for requesting drive API.


```
    _     ___   ___
   /_\   | _ \ |_ _|
  / _ \  |  _/  | |
 /_/ \_\ |_|   |___| 

   ___   _      ___   ___   _  _   _____
  / __| | |    |_ _| | __| | \| | |_   _|
 | (__  | |__   | |  | _|  | .` |   | |
  \___| |____| |___| |___| |_|\_|   |_|

  ___    ___    ___
 | __|  / _ \  | _ \
 | _|  | (_) | |   /
 |_|    \___/  |_|_\

   ___    ___     ___     ___   _      ___
  / __|  / _ \   / _ \   / __| | |    | __|
 | (_ | | (_) | | (_) | | (_ | | |__  | _|
  \___|  \___/   \___/   \___| |____| |___|

  ___    ___   ___  __   __  ___
 |   \  | _ \ |_ _| \ \ / / | __|
 | |) | |   /  | |   \ V /  | _|
 |___/  |_|_\ |___|   \_/   |___|

                   _
  __ _   _ _    __| |
 / _` | | ' \  / _` |
 \__,_| |_||_| \__,_|

  ___   _  _   ___   ___   _____   ___
 / __| | || | | __| | __| |_   _| / __|
 \__ \ | __ | | _|  | _|    | |   \__ \
 |___/ |_||_| |___| |___|   |_|   |___/

```
                                                                                    version 1.1
