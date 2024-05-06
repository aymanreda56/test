import requests
import json
import datetime
import dateutil.parser
import wget
import subprocess

r = requests.get("https://api.github.com/repos/aymanreda56/test/commits")

entry_date = r.json()[0]['commit']['author']['date']



with open(file="ver.txt", mode='r')as f:
    current_version_str = f.read()

current_version = dateutil.parser.parse(current_version_str)


latest_version = dateutil.parser.parse(entry_date)
if(current_version < latest_version):
    # url = 'http://github.com/aymanreda56/test/archive/main.zip'
    # filename = wget.download(url)
    subprocess.run('git pull https://github.com/aymanreda56/test')




with open(file="ver.txt", mode='w')as f:
    f.write(entry_date)
print(type(dateutil.parser.parse(entry_date)))


#commnt
