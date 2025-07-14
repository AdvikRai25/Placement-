import time
import sys
h=12
m=43
s=0
while True:
    sys.stdout.write(f"\r{h:02d}:{m:02d}:{s:02d}")
    sys.stdout.flush()
    time.sleep(1)
    s=s+1
    if(s==60):
        m=m+1
        s=0
    if (m==60):
        h=h+1
        m=0
    if(h==24):
        h=0