      _       _______  _____
     / \     |_   __ \|_   _|
    / _ \      | |__) | | |
   / ___ \     |  ___/  | |
 _/ /   \ \_  _| |_    _| |_
|____|_|____||_____| _|_____|_______  ____  _____  _________
 .' ___  ||_   _|   |_   _||_   __  ||_   \|_   _||  _   _  |
/ .'   \_|  | |       | |    | |_ \_|  |   \ | |  |_/ | | \_|
| |         | |   _   | |    |  _| _   | |\ \| |      | |
\ `.___.'\ _| |__/ | _| |_  _| |__/ | _| |_\   |_    _| |_
 `.____ .'|________||_____||________||_____|\____|  |_____|
 ________    ___   _______
|_   __  | .'   `.|_   __ \
  | |_ \_|/  .-.  \ | |__) |
  |  _|   | |   | | |  __ /
 _| |_    \  `-'  /_| |  \ \_
|_____|    `.___.'|____| |___|
 ______   _______     _____  ____   ____  ________
|_   _ `.|_   __ \   |_   _||_  _| |_  _||_   __  |
  | | `. \ | |__) |    | |    \ \   / /    | |_ \_|
  | |  | | |  __ /     | |     \ \ / /     |  _| _
 _| |_.' /_| |  \ \_  _| |_     \ ' /     _| |__/ |
|______.'|____|_|___||_____|  ___\_/_____|________|___  _________   ______
 .' _ '.     .' ____ \ |_   ||   _||_   __  ||_   __  ||  _   _  |.' ____ \
 | (_) '___  | (___ \_|  | |__| |    | |_ \_|  | |_ \_||_/ | | \_|| (___ \_|
 .`___'/ _/   _.____`.   |  __  |    |  _| _   |  _| _     | |     _.____`.
| (___)  \_  | \____) | _| |  | |_  _| |__/ | _| |__/ |   _| |_   | \____) |
`._____.\__|  \______.'|____||____||________||________|  |_____|   \______.'


                                                                                    version 1.0
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




