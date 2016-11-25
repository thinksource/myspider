from cfspider import *

if __name__="main":
    urllink="http://www.sydneytoday.com/house_rent"
    cf=cfspider(urllink)
    advertises=cf.work(1,10)
