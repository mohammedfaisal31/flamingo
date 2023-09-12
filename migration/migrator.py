import yaml
from replicator import * 
def load_config(yaml_file="../config/transformation-rules.yaml"):
    with open(yaml_file, "r") as file:
        config = yaml.safe_load(file)
    return config

def startMigration():
    config = load_config()
    migrate_table_to_mongo_collection(config['source_table_name'],config['dest_collection_name'])
    print("----------------------------------------END----------------------------------")
