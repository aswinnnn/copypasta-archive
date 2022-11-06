from json import loads
import requests
from datetime import datetime
from pathlib import Path 
import os

def get_last():
    fs = os.listdir(Path(f"{os.getcwd()}/pasta/"))
    ls = ( len(fs) - 1 ) + 1
    return ls 

bp = os.getcwd()
file = f"{get_last()}.txt"
p = Path(f"{bp}/pasta/{file}")

headers = {'User-agent': "Aswins lovely gh actions worker"}

url = "https://www.reddit.com/r/copypasta/top.json"
content = (requests.get(url, headers=headers)).json()

pasta = content['data']['children'][0]['data']['selftext']
title = content['data']['children'][0]['data']['title']

with open(p, "x", encoding='utf-8') as f:
    f.write(f"{title}\n\n{pasta}")

