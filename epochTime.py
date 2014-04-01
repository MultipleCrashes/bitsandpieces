
from datetime import datetime

import time;
#t = time.mktime(time.strptime("29.08.2011 11:05:02", "%d.%m.%Y %H:%M:%S"));

with open('Hashes-17.csv') as data:
    for lines in data:
        #print lines
        splitLines=lines.split(',')
        print splitLines[2]
        temp='"'+splitLines[2]+'"'
        #print temp
        #print datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
        epochTime=time.mktime(time.strptime(splitLines[2],"%Y-%m-%d %H:%M:%S.%f"))
        print epochTime
        print lines
        
