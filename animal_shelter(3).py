from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'smokey'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31229
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,31229))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Read method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            cursor = self.database.animals.find(data)
            return cursor
        else:
            raise Exception("Nothing to read, because data parameter is empty!")
            return False
        
# Update method to implement the R in CRUD.
    def update(self, data_x, data_y):
        if data_x and data_y is not None:
            result = self.database.animals.update_many({ '$set' : {data_x, data_y}})
            return result
        else:
            raise Exception("Nothing to read, because data parameters are empty!")
            return False
        
# Delete method to implement the R in CRUD.
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data)
            return result
        else:
            raise Exception("Nothing to read, because data parameter is empty!")
            return False