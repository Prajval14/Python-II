from pymongo import MongoClient

# Establishing a connection to the MongoDB server
client = MongoClient('localhost', 27017) #OR - client = MongoClient('mongodb://localhost:27017/')

# Create a new database
db = client['planetearth']

# Create a new collection (implicit vs explicit)
collection = db['mycollection'] #OR - collection = db.create_collection('mycollection')

# You can now check that the 'mycollection' exists
print('Collection created:', 'mycollection' in db.list_collection_names())

# Now list all the databases in MongoDB (with atleast one collection)
database_list = client.list_database_names()
print(database_list)

# Check if 'planetearth' exists in the list of databases
if 'planetearth' in database_list:
    print("'planetearth' exists.")
else:
    print("'planetearth' does not exist or has not been initialized with any data.")

# Inserting data in collections
result = db.mycollection.insert_one({'name': 'John', 'age': 30})

multiple_records = [
    {'name': 'John2', 'age': 35},
    {'name': 'John3', 'age': 36}
]

result2 = db.mycollection.insert_many(multiple_records)

# Print records output
print(f"{len(result.inserted_ids)} records were inserted.")
print("The inserted IDs are:", result.inserted_ids)