#!/usr/bin/python3

import os
import re
from datetime import datetime

try:
    max_size_gb = 200
    while True:
        arr = []
        files = [f for f in os.listdir('/home/User/web/backup') if os.path.isfile(os.path.join('/home/User/web/backup', f)) and not f.startswith('.')]
        for key, item in enumerate(files):
            arr.append(os.path.getsize(os.path.join('/home/User/web/backup', item)))
        current_size_gb = sum(arr) / pow(1024, 3)
        if current_size_gb <= max_size_gb:
            break
        else:
            arr_time = []
            for file in files:
                match = re.search(r'\d{8}', file)
                if match:
                    arr_time.append(match.group(0))
            oldest_file_date = list(set(arr_time))[0]
            for file in [f for f in os.listdir('/home/User/web/backup') if os.path.isfile(os.path.join('/home/User/web/backup', f)) and not f.startswith('.')]:
                match = re.search(r'\d{8}', file)
                if match and match.group(0) == oldest_file_date:
                    os.system('sudo rm -rf ' + os.path.join('/home/User/web/backup', file))
except Exception as e:
    with open('/home/User/web/error_log.txt', 'a') as f:
        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '  ' + str(e) + '\n')
