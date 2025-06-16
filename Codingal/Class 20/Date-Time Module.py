#Date-Time Module
import time
from datetime import datetime

x = datetime.now()
while True:
    time.sleep(1)
    print(x.now())