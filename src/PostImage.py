import os, uuid
import datetime
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

class PostImage:
    def __init__(self, timeStump: str):
        try:
            print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

            # Quick start code goes here
            connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

            # Create the BlobServiceClient object which will be used to create a container client
            blob_service_client = BlobServiceClient.from_connection_string(connect_str)

            # Create a unique name for the container
            container_name = str('image')

            # Create a local directory to hold blob data
            # local_file_name = timeStump + "_Lilium_bulbiferum.jpg"
            local_file_name = "1662px-Lilium_bulbiferum.jpg"
            upload_file_path = "/home/pi/Documents/python_project/TetraWatch/data/" + local_file_name
            # Create a blob client using the local file name as the name for the blob
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

            print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

            # Upload the created file
            with open(upload_file_path, "rb") as data:
                blob_client.upload_blob(data)
        except Exception as ex:
            print('Exception:')
            print(ex)