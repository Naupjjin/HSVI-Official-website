from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv
index_path =  os.path.dirname(os.path.abspath(__file__))

load_dotenv(index_path+"/tst.env")

print(os.getenv("password"),os.getenv('token'))



url = f"mongodb+srv://hsvi0919:Fx794j4sLWllGcho@hsvi.bquldrx.mongodb.net/?retryWrites=true&w=majority"



# news 
index_shownews_n = 3

# alert
alert_now={
    "message":"看看我們新推出的Vtuber",
    "bg-color":"rgba(144, 142, 142, 0.427)",
    "type":"info"
}