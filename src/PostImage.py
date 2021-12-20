import os, uuid
import datetime
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

class PostImage:
    def __init__(self, timeStump: str):
        try:
            print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

            connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

            blob_service_client = BlobServiceClient.from_connection_string(connect_str)

            container_name = str('image')

            local_file_name = timeStump + '.jpg'
            upload_file_path = '/home/pi/Source/TetraWatch/data/' + local_file_name
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

            print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

            # Upload the created file
            with open(upload_file_path, "rb") as data:
                blob_client.upload_blob(data)
        except Exception as ex:
            print('Exception:')
            print(ex)
        finally:
            print('finally: Image delete!')
            os.remove('/home/pi/Source/TetraWatch/data/' + timeStump + '.jpg')
