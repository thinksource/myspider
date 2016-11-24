import csv

class rentads:
    def __init__(self, url,title):
        self.inside={}
        self.inside["url"]=url
        self.inside["title"]=title

    def setaddr(self, addr):
        self.inside["address"]=addr

    def setprice(self,price):
        self.inside["price"]=price

    def setproperty_type(self, p):
        self.inside["property_type"]=p

    def setcontact_person(self, p):
        self.inside["contact_person"]=p

    def setcontact_telephone(self, p):
        self.inside["contact_telephone"]=p

    def setaddentails(self,p):
        self.inside["details"]=p

    def setroom_type(self,p):
        self.inside["room_type"]=p

    def setpics(self, p):
        self.inside['pic_urls']=p

    def appendfile(self):
        with open(self.filename, 'w') as csvfile:
            fieldnames=[ 'title', 'url',"address","price", "property_type","room_type",'contact_person', 'contact_telephone','details','pic_urls']
            writer=csv.Dictwriter(csvfile, fieldnames=fieldnames)
            #writer.writeheader()
            writer.writerrow(self.inside)
