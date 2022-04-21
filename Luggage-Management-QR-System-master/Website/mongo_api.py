import pymongo
from bson import ObjectId
import dns
import gridfs


connection = None
database = None
QR_Gen_Accounts = None
QR_Read_Accounts = None
Flights = None
Luggage = None
Complaint = None
user_db = None

def get_obj_id(id):
    return ObjectId(id)

def main():
    global connection
    global database
    global QR_Gen_Accounts
    global QR_Read_Accounts
    global Flights
    global Luggage
    global Complaint
    global user_db
    global qr_db
    global grid_fs
    global helpdesk_db
    # connection_String = "mongodb://shaunak:<password>@cluster0-shard-00-00.egwkk.mongodb.net:27017,cluster0-shard-00-01.egwkk.mongodb.net:27017,cluster0-shard-00-02.egwkk.mongodb.net:27017/test?replicaSet=Cluster0-shard-0&ssl=true&authSource=admin"
    # client = pymongo.MongoClient(connection_String)
    client = pymongo.MongoClient(host = 'localhost', port = 27017)
    db = client.Tarp_project
    print("working")
    
    QR_Read_Accounts = db.QR_Read_Accounts
    QR_Gen_Accounts = db.QR_Gen_Accounts
    Flights = db.Flights
    Luggage = db.Luggage
    Complaint = db.Complaint
    user_db = db.user_db
    qr_db = db.QRs
    helpdesk_db = db.Helpdesk
    grid_fs = gridfs.GridFS(db)