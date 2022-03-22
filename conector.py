from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

import mysql.connector
import dbase

def main():
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
        results = service.files().list(pageSize=1,fields="*").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
            return
        print('Files:')

        mydb = basedatos()

        for item in items:
            #nombre del archivo, la extensión, el owner del archivo, la visibilidad (público o privado) y la fecha de última modificación.   
            print("Nombre del Archivo: ",item['name']," | Tipo de Archivo: " , item['mimeType'], " | Owner: ",item['owners'][0]['displayName']," | Ultima Modificacion: ", item['modifiedTime'])
            name = item['name']
            filetype = item['mimeType']
            owner = item['owners'][0]['displayName']
            lastmod = item['modifiedTime']
            insert_varibles_into_table(mydb, name, filetype,owner,lastmod)


    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


def basedatos():
    mydb = mysql.connector.connect(
        host=dbase.servidor,
        database=dbase.database,
        user=dbase.user,
        password=dbase.pswd
    )  
    print(mydb)
    print('Conexion Exitosa!')
    return mydb

def insert_varibles_into_table(connection, name, type, owner, mod_date):
    try:
        cursor = connection.cursor()
        mySql_insert_query = "INSERT INTO archivos (nombre, tipo, owner, u_modificacion) VALUES (%s, %s, %s, %s) "
        record = (name, type, owner, mod_date)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into archivos table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == '__main__':
    main()