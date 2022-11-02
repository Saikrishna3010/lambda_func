def lambda_handler(event, context):
    # TODO implement
    
    #os.environ['TZ']='UTC'
    #print('printing the input file name')
    #print(event['loc'])
    
    timestamp = dt.datetime.now().strftime("%s")
    filename_json = "/tmp/file_{ts}.json".from __future__ import print_function
import json
import datetime as dt
from datetime import date
import time



format(ts=timestamp)
    filename_csv = "/tmp/file_{ts}.csv".format(ts=timestamp)
    LOCAL_FILE = '/tmp/test_{ts}.txt'.format(ts=timestamp)
    filename_json_final = "/tmp/file_final_{ts}.json".format(ts=timestamp)
    print(dt.datetime.now())
    start_time = dt.datetime.now() + dt.timedelta(minutes=280)
    start_time_yr = start_time.year
    start_time_month = '{:02d}'.format(start_time.month)
    start_time_day = '{:02d}'.format(start_time.day)
    start_time_hour = '{:02d}'.format(start_time.hour)
    start_time_min = '{:02d}'.format(start_time.minute)
    start_time_sec = '{:02d}'.format(start_time.second)
    
    print(start_time)
    start_time_epoch=int(time.mktime(time.strptime((str(start_time_yr)+str(start_time_month)+str(start_time_day)+str(start_time_hour)+str(start_time_min)+str(start_time_sec)), '%Y%m%d%H%M%S')))
    print(start_time_epoch-19800)
    
    print(dt.datetime(2022, 11, 1, 16, 29, 0).timestamp())
    print('Sai')