from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 100 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        """
        results = service.files().list(
            pageSize=5, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            #nombre del archivo, la extensión, el owner del archivo, la visibilidad (público o privado) y la fecha de última modificación.   
            print(u'{0} ({1})'.format(item['name'], item['id']))
        """


        """
        files = service.files().list().execute().get('files', [])
        for f in files:
             #nombre del archivo, la extensión, el owner del archivo, la visibilidad (público o privado) y la fecha de última modificación.
            print("Nombre del Archivo: ",f['name']," Tipo de Archivo: " , f['mimeType'])
            # output: {'kind': 'drive#file', 'id': '1k7OJW_gDyiYNJRZk8bZr1-74cOxEI4Jm', 'name': 'Teoria.rar', 'mimeType': 'application/rar'}
        """

        
        results = service.files().list(pageSize=1, fields="*").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            #nombre del archivo, la extensión, el owner del archivo, la visibilidad (público o privado) y la fecha de última modificación.   
                #print(u'{0} ({1})'.format(item['name'], item['id']))
            #print(item)
            print("Nombre del Archivo: ",item['name']," | Tipo de Archivo: " , item['mimeType'], " | Owner: ",item['owners'][0]['displayName']," | Ultima Modificacion: ", item['modifiedTime'])

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    main()