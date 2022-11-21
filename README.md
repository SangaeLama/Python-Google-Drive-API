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


                                                                                    version 1.1
Drive API V3 and Sheets API V4

On Google Cloud Console:
    1. Enable the Drive API and Sheets API.
    2. Create an Oauth 2.0 Client ID and download&rename it as client-secret.json in the working directory

At Client Side:
    1. Install python libraries at client side.
        ```bash
        pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib pandas pickle
        ```
    2. Edit the python files to specify where the file should be uploaded by editing the folder_id, and driveID if working with Shared Drives.

Usage:
    1. Run the following command:
        ```$python3 file_uploader.py x.png```
        where x.png is the file to be uploaded.


V1.1:
    Added support of service accounts instead of just Oauth2.0 tokens for requesting drive API.

