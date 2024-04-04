from pymongo import MongoClient
from __init__ import url,index_path
from PIL import Image
import io
import datetime

class DB():
    def __init__(self,_url) -> None:
        self.client = MongoClient(_url,tls=True,tlsAllowInvalidCertificates=True)
        self.db = self.client['hsvi']
        self.collection = self.db['announcement']
    
    def load_news(self,_n:int=3)->tuple:
        _n=1
        sorted_documents = self.collection.find().sort('time',-1)
        _announce = tuple()
        # if len(list(sorted_documents))<_n:
        #     _n=len(list(sorted_documents))
        print(self.collection.count_documents({"time":1},skip = _n))
        print(f"announce({self.collection.count_documents({},skip = _n)}) less less than{_n}")
        for i in range(_n):
            _announce+=(sorted_documents[i]['title'],)
            image =self.collection.find_one({"time":sorted_documents[i]['time']})
            pil_img = Image.open(io.BytesIO(image['img']))
            pil_img.save(f"{index_path}/static/img/announcement/time_{i}.png")
        return _announce
    
    def add_news(self,img:Image,title:str,time)->None:
        _data = {
            "title":title,
            "time":time,
            "img":img
        }
        self.collection.insert_one(_data)

db = DB(url)

