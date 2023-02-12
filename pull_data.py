import json
import urllib.request
import pandas as pd
import numpy as np
from datetime import datetime
import time

def parse_with_time_stamp(url):
    x = urllib.request.urlopen(url)
    raw_data = x.read()
    utc_now = datetime.utcnow()

    encoding = x.info().get_content_charset('utf8')  # JSON default
    data = json.loads(raw_data.decode(encoding))

    return data, utc_now

train_url = 'https://www3.septa.org/api/TrainView/index.php'
transit_url = 'https://www3.septa.org/api/TransitViewAll/index.php'

while True:
    #train_data, train_now = parse_with_time_stamp(train_url)
    #train_data = pd.DataFrame(train_data).assign(timestamp = train_now)
    transit_data, transit_now = parse_with_time_stamp(transit_url)
    transit_data = pd.concat([(pd.DataFrame(v)).assign(route=k) for k,v in transit_data['routes'][0].items()])
    transit_data.timestamp = pd.to_datetime(transit_data.timestamp, origin = "unix",unit = "s")
    transit_data.to_csv('transit_data.csv',index=False,mode="a",header=False)
    time.sleep(30)