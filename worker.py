from json import loads
import urllib3
from datetime import datetime
from pathlib import Path 

file = datetime.now().strftime('%d_%m_%Y.txt')

http = urllib3.PoolManager()
url = "https://www.reddit.com/r/copypasta/top.json"
content = http.request('GET', url)
content = loads(content.data.decode('utf-8'))

pasta = content['data']['children'][0]['data']['selftext']
title = content['data']['children'][0]['data']['title']

with open(Path(f"\pasta\{file}"), "x", encoding='utf-8') as f:
    f.write(f"{title}\n\n{pasta}")

