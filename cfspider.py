from sydneytoday import CloudflareScraper as cfscraper
import requests
from bs4 import BeautifulSoup
import urllib
import csv
from rentads import rentads
class cfspider:
    def __init__(self, listurltemplate):
        self.root_url="http://www.sydneytoday.com"
        self.mysession=requests.session()
        # print(self.mysession)
        self.scraper=cfscraper.create_scraper(sess=requests.session())
        self.listurl=listurltemplate
        self.filename="address.csv"
        #soup = BeautifulSoup()

    def getlist(self, mydic):
        result=self.scraper.get(self.listurl+"?"+urllib.parse.urlencode(mydic))
        if(result.status_code==200):
            soup = BeautifulSoup(result.content, 'html.parser')
            relist=soup.find_all('li', "trAA price-pic-new-style")
            return relist

    def getpage(self, pageurl, adobj):
        pageresult=self.scraper.get(pageurl)
        soup = BeautifulSoup(pageresult.content, 'html.parser')
        table_pre=soup.find('td', id="becan_l")
        table = table_pre.find('table')
        table_body=table.find('tbody')
        rows=table_body.find_all('tr')
        pic_urls=[]
        for row in rows:
            cols=row.find_all('td')
            for col in cols:
                colstr=getattr(col, 'string', None)
                if colstr==u"具体地址":
                    address_col=col.next_element
                    address=address_col.string
                    adobj.setaddr(address)
                if colstr== u"房屋设备":
                    facility_col=col.next_element
                    facility=facility_col.string


        table2=soup.find('div',id='list_middle').next_element.next_element
        table_body=table2.find('tbody')
        rows=table_body.find_all("tr")
        row=rows[2]
        row_text=row.tr.td.div.p.string
        adobj.setdetails(row_text)

        pic_div=soup.find('div', id="divmov")
        pic_tr=pic_div.find('table').find('tbody').find('table').find('tbody').find('tr')
        cols=pic_tr.find_all('td')
        for col in cols:
            link=col.find(a)
            pic_urls.append(link['href'])
        adobj.setpics(pic_urls)
        return adobj

    def parse(self,part):
        # part=BeautifulSoup(partstr)
        frontimage_url_tag=part.find('div','single-news-image')
        frontimage_url=frontimage_url_tag.a.img["src"]
        inform=part.find('div','single-news-meta')
        informlist=inform.children
        suburb=None
        property_type=None
        contact_person=None
        title=None
        rentlist=[]
        # f=open('temp2.html','wb')
        for i in inform.children:
            rentad=None
            if hasattr(i, 'a'):
                # f.write(i.a.string)
                # f.write(u"\n")
                if hasattr(i.a, 'font'):
                    title=i.a.font.string
                    url=self.root_url+i.a['href']
                    print(url)
                    rentad=rentads(url, title)
            if hasattr(i, 'div'):
                if i["class"]=="fenlei-meta first" and suburb==None:
                    suburb=i.find_all('span')[1].string
                    rentad.setsub(suburb)
                elif i["class"]=="fenlei-meta middle" and property_type==None:
                    property_type=i.find_all('span')[1].string
                    rentad.setproperty_type(property_type)
                elif i["class"]=="fenlei-meta last" and room_type==None:
                    room_type=i.find_all('span')[1].string
                    rentad.setroom_type(room_type)
                elif i["class"]=="fenlei-meta middle" and contact_person==None:
                    contact_person=i.find_all('span')[1].string
                    rentad.setcontact_person(contact_person)
                elif i["class"]=="fenlei-meta last" and contact_telephone==None:
                    contact_telephone=i.find_all('span')[1].string
                    rentad.setcontact_telephone(contact_telephone)
            price_tag=part.find('div','single-news-price-tag')
            price_str=price_tag.div.string
        # f.close(
            if rentad!=None:
                rentad.setprice(price_str)
                # self.getpage(url, rentad)
                rentlist.append(rentad)
        return rentlist



    def work(self,listurltemplate, frompage, endpage):
        self.listurl=listurltemplate
        for i in range(frompage, endpage):
            mydic={"page":str(i)}
            partlist=getlist(self, mydic)
            for j in partlist:
                rentad=parse(self,j)
                getpage(self, rentad.inside["url"],rentad)
