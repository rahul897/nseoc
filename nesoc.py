import requests
import json
import traceback
from datetime import datetime
import os

indices = ['BANKNIFTY']
equities = ['BHEL']
base_url = "https://www.nseindia.com/"
index_url = "https://www.nseindia.com/api/option-chain-indices?symbol={}"
equity_url = "https://www.nseindia.com/api/option-chain-equities?symbol={}"

root_dir=""
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    'accept-encoding': 'gzip, deflate, br'
}
try:
    session = requests
    request = session.get(base_url, headers=headers, timeout=10)
    cookies = dict(request.cookies)
    for index in indices:
        url = index_url.format(index)
        resp = requests.Session().get(url, headers=headers, timeout=10, cookies=cookies )
        data = resp.json()
        data.pop('filtered')
        data = data['records']
        path = os.path.join(root_dir, str(datetime.now().date()))
        os.makedirs(path, exist_ok=True)
        ref_time = data['timestamp']
        d = datetime.strptime(ref_time, "%d-%b-%Y %H:%M:%S")
        d = d.strftime("%d%m%Y_%H%M%S")
        with open(os.path.join(path,d+'.json'),'w') as f:
            json.dump(data,f)
except:
    traceback.print_exc()
    
#crontab
#* 10-16 * * * python nseoc.py
