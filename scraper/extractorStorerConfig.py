from pymongo import MongoClient

add = "localhost"
port = 27017
db = "get_cancion_primary_db"
collection = "lyrics"
mongoclientObj = MongoClient(add,port)[db][collection]

base_url = "http://www.allthelyrics.com"
index_url = "http://www.allthelyrics.com/index"
alphabets = list("abcdefghiklmnopqrstuvwxyz")
alphabets.append("numbers")