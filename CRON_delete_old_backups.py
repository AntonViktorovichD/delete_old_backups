#!/usr/bin/python3

from datetime import datetime, timedelta
import os
i = 3
while i < 10:
        for filename in os.listdir('/home/grand/web/grandgold.jewelry/public_html/bitrix/backup'):
            if filename.find((datetime.now() - timedelta(days = i)).strftime('%Y%m%d')) != -1:
                os.remove(f'/home/grand/web/grandgold.jewelry/public_html/bitrix/backup/{filename}')
i += 1
