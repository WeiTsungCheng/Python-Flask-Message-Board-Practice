from datetime import datetime
from dateutil import tz

print(datetime.utcnow())
print(datetime.now())

utc_zone = tz.gettz('UTC')
tw_zone = tz.gettz('Asia/Taipei')
utc = datetime.utcnow()
utc = utc.replace(tzinfo=utc_zone)
print('轉換前：', utc.strftime('%Y/%m/%d %H:%M'))
tw_time = utc.astimezone(tw_zone)
print('轉換後：', tw_time.strftime('%Y/%m/%d %H:%M'))

