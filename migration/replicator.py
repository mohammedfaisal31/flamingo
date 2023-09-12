import sys
import datetime
import decimal
from tqdm import tqdm


sys.path.append("../")
from mappers import mysql_connector
from mappers import mongodb_connector

def migrate_table_to_mongo_collection(mysql_table_name, mongo_collection_name):
    
    #MySQL cursor
    mysql_cursor = mysql_connector.get_mysql_connection().cursor()
    
    #Mongo Config
    mongo_db = mongodb_connector.get_mongodb_connection()
    mongo_collection = mongo_db[mongo_collection_name]

    # MySQL Query to fetch data from the table
    mysql_query = f"SELECT * FROM {mysql_table_name}"
    mysql_cursor.execute(mysql_query)

    # Fetch all rows from MySQL Table
    mysql_rows = mysql_cursor.fetchall()
    # Iterate through MySQL rows and insert into MongoDB
    
    progress_bar = tqdm(total=len(mysql_rows), desc=f"Migrating table {mysql_table_name} -> {mongo_collection_name}")
    for row in mysql_rows:
        processed_row = {key: convert_to_mongodb_compatible(value) for key, value in row.items()}
        mongo_collection.insert_one(processed_row)
        progress_bar.update(1)
    progress_bar.close()
    print("Finished process\n")

    # Close MySQL and MongoDB connections
    mysql_cursor.close()



# Function to convert data types for MongoDB
def convert_to_mongodb_compatible(value):
    if isinstance(value,datetime.date):
        return datetime.datetime.strptime(value.strftime("%Y %M %d"),"%Y %M %d")
    elif isinstance(value,decimal.Decimal):
        return float(value)    
    else:
        return value


