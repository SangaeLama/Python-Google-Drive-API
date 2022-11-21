           _____  _____
     /\    |  __ \|_   _|
    /  \   | |__) | | |
   / /\ \  |  ___/  | |
  / ____ \ | |     _| |_
 /_/____\_\|_|    |_____|______  _   _  _______
  / ____|| |     |_   _||  ____|| \ | ||__   __|
 | |     | |       | |  | |__   |  \| |   | |
 | |     | |       | |  |  __|  | . ` |   | |
 | |____ | |____  _| |_ | |____ | |\  |   | |
  \_____||______||_____||______||_| \_|   |_|
 |  ____|/ __ \ |  __ \
 | |__  | |  | || |__) |
 |  __| | |  | ||  _  /
 | |    | |__| || | \ \
 |_|___  \____/ |_|__\_\__      __ ______
 |  __ \ |  __ \ |_   _|\ \    / /|  ____|
 | |  | || |__) |  | |   \ \  / / | |__
 | |  | ||  _  /   | |    \ \/ /  |  __|
 | |__| || | \ \  _| |_    \  /   | |____
 |_____/ |_|__\_\|_____|_  _\/___ |______| _______  _____
   ___     / ____|| |  | ||  ____||  ____||__   __|/ ____|
  ( _ )   | (___  | |__| || |__   | |__      | |  | (___
  / _ \/\  \___ \ |  __  ||  __|  |  __|     | |   \___ \
 | (_>  <  ____) || |  | || |____ | |____    | |   ____) |
  \___/\/ |_____/ |_|  |_||______||______|   |_|  |_____/


Drive API V3 and Sheets API V4

On Google Cloud Console:
    1. Enable the Drive API and Sheets API.
    2. Create an Oauth 2.0 Client ID and download&rename it as client-secret.json in the working directory

At Client Side:
    1. Install python libraries at client side.
        ```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib pandas pickle```
    2. Edit the python files to specify where the file should be uploaded by editing the folder_id, and driveID if working with Shared Drives.

Usage:
    1. Run the following command:
        ```$python3 file_uploader.py x.png```
        where x.png is the file to be uploaded.




