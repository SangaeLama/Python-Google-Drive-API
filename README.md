# Python Google Drive API
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

Usage:
    1. Run the following command:
        ```bash
        python3 file_uploader.py x.png

        where x.png is the file to be uploaded.


V1.1:
    Added support of service accounts instead of just Oauth2.0 tokens for requesting drive API.


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

### 1. `file_uploader.py`

This script allows you to upload files to a specific Google Drive folder. It provides options to handle duplicate files and scans the destination folder for duplicates before uploading.

Usage:
```bash
python file_uploader.py <file_to_upload>


