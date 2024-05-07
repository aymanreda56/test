# Possible Errors

# There are numerous errors that can cause the updating process to fail.

# If the user’s PC is behind a proxy, the download of the manifest file or zip file may fail; to avoid this, whitelist the URLs where the manifest file and zip file are hosted.
# If the user’s PC lacks the necessary storage, the download of the zip file or extraction of the zip file may fail. To avoid this, instruct the user to keep enough disc space.
# If the updater does not have the required permissions, the killing process of application may fail. To avoid this make sure updater and application are running with the same user permissions.
# Copying the executables may fail if the application is not stopped properly.
# Because of the partial copy, restarting the application may fail; to avoid this, make the upgrading process atomic, as we discussed in the previous section.






import requests
import os
import shutil
import json
import datetime
import dateutil.parser
import wget
import subprocess
from zipfile import ZipFile






def move_files_inside_folder_to_outside(folder_path):
    # Get a list of all files inside the folder
    files = os.listdir(folder_path)
    
    # Move each file to the parent directory
    for file_name in files:
        # Construct the source and destination paths
        source = os.path.join(folder_path, file_name)
        destination = os.path.join(os.path.dirname(folder_path), file_name)
        
        # Move the file
        shutil.move(source, destination)
    
    os.remove(folder_path)










r = requests.get("https://api.github.com/repos/aymanreda56/test/commits")

entry_date = r.json()[0]['commit']['author']['date']



with open(file="ver.txt", mode='r')as f:
    current_version_str = f.read()

current_version = dateutil.parser.parse(current_version_str)


latest_version = dateutil.parser.parse(entry_date)
if(current_version <= latest_version):
    url = 'http://github.com/aymanreda56/test/archive/main.zip'
    filename = wget.download(url)
    print(filename)
    new_version_zipfile_path = os.path.join(os.getcwd(), filename)

    # subprocess.run('git pull')

    with ZipFile(filename, 'r') as zObject: 
  
        # Extracting all the members of the zip  
        # into a specific location. 
        temp_dir = os.path.join(os.getcwd(), 'temp')
        if(not os.path.exists(temp_dir)):
            os.mkdir(temp_dir)
        zObject.extractall()

        new_version_folder, extension = os.path.splitext(new_version_zipfile_path)

        move_files_inside_folder_to_outside(new_version_folder)
    
    os.remove(new_version_zipfile_path)
    os.remove(temp_dir)



    with open(file="ver.txt", mode='w')as f:
        f.write(entry_date)


#saa

