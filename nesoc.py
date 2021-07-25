import requests
import json
import traceback
from datetime import datetime
import os

indices = ['BANKNIFTY','NIFTY','FINNIFTY']
equities = [
'AARTIIND',
'ABFRL',
'ACC',
'ADANIENT',
'ADANIPORTS',
'ALKEM',
'AMARAJABAT',
'AMBUJACEM',
'APLLTD',
'APOLLOHOSP',
'APOLLOTYRE',
'ASHOKLEY',
'ASIANPAINT',
'AUBANK',
'AUROPHARMA',
'AXISBANK',
'BAJAJ-AUTO',
'BAJAJFINSV',
'BAJFINANCE',
'BALKRISIND',
'BANDHANBNK',
'BANKBARODA',
'BATAINDIA',
'BEL',
'BERGEPAINT',
'BHARATFORG',
'BHARTIARTL',
'BHEL',
'BIOCON',
'BOSCHLTD',
'BPCL',
'BRITANNIA',
'CADILAHC',
'CANBK',
'CHOLAFIN',
'CIPLA',
'COALINDIA',
'COFORGE',
'COLPAL',
'CONCOR',
'COROMANDEL',
'CUB',
'CUMMINSIND',
'DABUR',
'DEEPAKNTR',
'DIVISLAB',
'DLF',
'DRREDDY',
'EICHERMOT',
'ESCORTS',
'EXIDEIND',
'FEDERALBNK',
'GAIL',
'GLENMARK',
'GMRINFRA',
'GODREJCP',
'GODREJPROP',
'GRANULES',
'GRASIM',
'GUJGASLTD',
'HAVELLS',
'HCLTECH',
'HDFC',
'HDFCAMC',
'HDFCBANK',
'HDFCLIFE',
'HEROMOTOCO',
'HINDALCO',
'HINDPETRO',
'HINDUNILVR',
'IBULHSGFIN',
'ICICIBANK',
'ICICIGI',
'ICICIPRULI',
'IDEA',
'IDFCFIRSTB',
'IGL',
'INDHOTEL',
'INDIGO',
'INDUSINDBK',
'INDUSTOWER',
'INFY',
'IOC',
'IRCTC',
'ITC',
'JINDALSTEL',
'JSWSTEEL',
'JUBLFOOD',
'KOTAKBANK',
#'L&amp;TFH',
'LALPATHLAB',
'LICHSGFIN',
'LT',
'LTI',
'LTTS',
'LUPIN',
#'M&amp;M',
#'M&amp;MFIN',
'MANAPPURAM',
'MARICO',
'MARUTI',
'MCDOWELL-N',
'METROPOLIS',
'MFSL',
'MGL','MINDTREE',
'MOTHERSUMI',
'MPHASIS',
'MRF',
'MUTHOOTFIN',
'NAM-INDIA',
'NATIONALUM',
'NAUKRI',
'NAVINFLUOR',
'NESTLEIND',
'NMDC',
'NTPC',
'ONGC',
'PAGEIND',
'PEL',
'PETRONET',
'PFC',
'PFIZER',
'PIDILITIND',
'PIIND',
'PNB',
'POWERGRID',
'PVR',
'RAMCOCEM',
'RBLBANK',
'RECLTD',
'RELIANCE',
'SAIL',
'SBILIFE',
'SBIN',
'SHREECEM',
'SIEMENS',
'SRF',
'SRTRANSFIN',
'SUNPHARMA',
'SUNTV',
'TATACHEM',
'TATACONSUM',
'TATAMOTORS',
'TATAPOWER',
'TATASTEEL',
'TCS',
'TECHM',
'TITAN',
'TORNTPHARM',
'TORNTPOWER',
'TRENT',
'TVSMOTOR',
'UBL',
'ULTRACEMCO',
'UPL',
'VEDL',
'VOLTAS',
'WIPRO',
'ZEEL']
base_url = "https://www.nseindia.com/"
index_url = "https://www.nseindia.com/api/option-chain-indices?symbol={}"
equity_url = "https://www.nseindia.com/api/option-chain-equities?symbol={}"

root_dir = ""
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
        resp = requests.Session().get(url, headers=headers, timeout=10, cookies=cookies)
        data = resp.json()
        data.pop('filtered')
        data = data['records']
        path = os.path.join(root_dir, str(datetime.now().date()))
        os.makedirs(path, exist_ok=True)
        ref_time = data['timestamp']
        d = datetime.strptime(ref_time, "%d-%b-%Y %H:%M:%S")
        d = d.strftime("%d%m%Y_%H%M%S")
        with open(os.path.join(path, d + '_' + index + '.json'), 'w') as f:
            json.dump(data, f)

    for equity in equities:
        url = equity_url.format(equity)
        resp = requests.Session().get(url, headers=headers, timeout=10, cookies=cookies)
        data = resp.json()
        data.pop('filtered')
        data = data['records']
        path = os.path.join(root_dir, str(datetime.now().date()))
        os.makedirs(path, exist_ok=True)
        ref_time = data['timestamp']
        d = datetime.strptime(ref_time, "%d-%b-%Y %H:%M:%S")
        d = d.strftime("%d%m%Y_%H%M%S")
        with open(os.path.join(path, d + '_' + equity + '.json'), 'w') as f:
            json.dump(data, f)
except:
    traceback.print_exc()
