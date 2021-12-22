import os
from datetime import date
from dateutil.rrule import rrule, DAILY

START_DATE = date(2009, 5, 30)
FULL_PATH = "C:\\Users\\Chiemerie\\Pictures\\Test\\"

list = [x for x in os.listdir(FULL_PATH)]
count = 0

for dt in rrule(DAILY, dtstart=START_DATE):
    for num in range(2):
        dst = dt.strftime("%d %m %Y") + ".jpg"
        src = FULL_PATH + list[count]
        dst = FULL_PATH + dst

        if os.path.isfile(dst):
            os.rename(src, dst + " (1)")
        else:
            os.rename(src, dst)
        count += 1