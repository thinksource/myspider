
#!/usr/bin/env python3

from cfspider import *

if __name__=="__main__":
    urllink="http://www.sydneytoday.com/house_rent"
    cf=cfspider(urllink)
    advertises=cf.work(0,10)
    for i in advertises:
        print(i)
