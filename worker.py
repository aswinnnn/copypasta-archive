from json import loads
import requests
from datetime import datetime
from pathlib import Path 
import os

bp = os.getcwd()
file = datetime.now().strftime('%d_%m_%Y.txt')
p = Path(f"{bp}/pasta/{file}")

headers = {'User-agent': "Aswins lovely gh actions worker"}

url = "https://www.reddit.com/r/copypasta/top.json"
content = (requests.get(url, headers=headers)).json()

pasta = content['data']['children'][0]['data']['selftext']
title = content['data']['children'][0]['data']['title']

with open(p, "x", encoding='utf-8') as f:
    f.write(f"{title}\n\n{pasta}")

