import requests
import json
import datetime
import dateutil.parser
import wget
import subprocess
import shutil, os


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



r = requests.get("https://api.github.com/repos/aymanreda56/test/commits")

entry_date = r.json()[0]['commit']['author']['date']



with open(file="ver.txt", mode='r')as f:
    current_version_str = f.read()

current_version = dateutil.parser.parse(current_version_str)


latest_version = dateutil.parser.parse(entry_date)
if(current_version < latest_version):
    # url = 'http://github.com/aymanreda56/test/archive/main.zip'
    # filename = wget.download(url)
    subprocess.run('git clone https://github.com/aymanreda56/test')
    folder_path = "test"
    move_files_inside_folder_to_outside(folder_path)
    shutil.rmtree('test')








with open(file="ver.txt", mode='w')as f:
    f.write(entry_date)
print(type(dateutil.parser.parse(entry_date)))

