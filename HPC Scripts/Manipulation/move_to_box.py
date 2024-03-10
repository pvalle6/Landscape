"""
This script provides for iterating through the structural predictions folder and backing up the ~1.5 TB data
to the box using API (DO NOT COMMIT THE BOX API KEY TO GITHUB).
"""

import os
import os
from boxsdk import OAuth2, Client
import requests
import argparse

argparse = argparse.ArgumentParser(description='Upload files to Box')
argparse.add_argument('local_folder_path', type=str, help='Path to the local folder to upload')
argparse.add_argument('upload_begin', type=int, help='first file index to upload')
argparse.add_argument('upload_end', type=int, help='last file index to upload')

args = argparse.parse_args()
local_folder_path = str(args.local_folder_path)
upload_begin = int(args.upload_begin)
upload_end = int(args.upload_end)


# Set your Box application credentials
CLIENT_ID = 'g1wopj3w0burjirmhxyoj8heun181y01'
CLIENT_SECRET = 'tHxLECdwRtYnAlLZJHMYATmOes9fnSMc'

FOLDER_ID = 252059722886  # Target folder ID
ENTERPRISE_ID = "MOeEykH6HJFlE0dR36UdSH4OIMxVPSGo" # Your Box enterprise ID
def get_access_token(client_id, client_secret, enterprise_id):
    # Box API endpoint for token retrieval
    token_url = "https://api.box.com/oauth2/token"

    # Request parameters
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "box_subject_type": "enterprise",
        "box_subject_id": enterprise_id
    }

    try:
        # Make the POST request to obtain the access token
        response = requests.post(token_url, data=payload)

        if response.status_code == 200:
            # Parse the JSON response
            token_data = response.json()
            access_token = token_data.get("access_token")
            print(f"Access token: {access_token}")
            return access_token
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")


def upload_file(file_path, folder_id, client):
    """
    Uploads a file to Box using the upload API
    """

    # Upload the file
    uploaded_file = client.folder(folder_id).upload(file_path, file_path)

    print(f"File '{uploaded_file.name}' uploaded successfully!")

# access_token = get_access_token(CLIENT_ID, CLIENT_SECRET, ENTERPRISE_ID)
file_names = os.listdir(local_folder_path)

oauth2 = OAuth2(CLIENT_ID, CLIENT_SECRET, access_token="vO1Wc43jE7lziIThbGinSoEcbgUNnhFC")
client = Client(oauth2)

for file_name in file_names[upload_begin:upload_end]:
    file_path = os.path.join(local_folder_path, file_name)
    upload_file(file_path, folder_id=FOLDER_ID, client=client)
