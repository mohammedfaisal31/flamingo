import sys
import time
import os
import yaml
import getpass


sys.path.append('../')
from  utils import art

def printTitle():
    print("+---------------------------------------------------------------+")
    art.textArt("Migration tool")
    print("+---------------------------------------------------------------+")


def loading_spinner(seconds, message="Please wait", symbol="⠋"):
    for _ in range(int(seconds)):
        sys.stdout.write(f"\r\033[91m{message} \033[0m{symbol}")  
        sys.stdout.flush()
        time.sleep(0.1)
        symbol = symbol[-1] + symbol[:-1]  
    sys.stdout.write('\r\033[0m')  
    sys.stdout.flush()

def printAbility():
    print("Migrate any MySQL db to mongodb with or without retaining relations")

def get_db_input_and_create_config(config_folder="../config", config_file="db-config.yaml"):
    if not os.path.exists(config_folder):
        os.makedirs(config_folder)

    config_path = os.path.join(config_folder, config_file)

    #Get MYSQL connection details
    configs = {}
    configs['mysql'] = {}
    print("\n--------------Enter SOURCE MYSQL DB connection details--------------")
    
    #Host
    print("Enter host:")
    configs['mysql']['host'] = input()
    
    #Port number
    print("Enter port:")
    configs['mysql']['port'] = int(input())
    
    #username
    print("Enter username:")
    configs['mysql']['user'] = input()
    
    #Password
    configs['mysql']['password'] = get_password()
    
    #DB name
    print("Enter db name:")
    configs['mysql']['database'] = input()
    
    
    print("\n--------------Enter TARGET MONGO-DB connection details--------------")
    configs['mongodb'] = {}
    #Host
    print("Enter host:")
    configs['mongodb']['host'] = input()
    
    #Port number
    print("Enter port:")
    configs['mongodb']['port'] = int(input())
    
    print("Auth not enabled by default")
    
    #DB name
    print("Enter db name:")
    configs['mongodb']['database'] = input()

    with open(config_path, 'w') as yaml_file:
        yaml.dump(configs, yaml_file, default_flow_style=False)

    print("------------------------DB Configurations finished------------------")


def selectTables(config_folder="../config", config_file="transformation-rules.yaml"):
    config_path = os.path.join(config_folder, config_file)
    configs = {}
    
    print("Enter the name of the source table you want to replicate/migrate:")
    configs['source_table_name'] = input()
    
    print("Enter the name of the destination collection you want to replicate to:")
    configs['dest_collection_name'] = input()
    
    with open(config_path, 'w') as yaml_file:
        yaml.dump(configs, yaml_file, default_flow_style=False)
    print("Saved configs")




def get_password():
    try:
        password = getpass.getpass(prompt="Enter password: ")
        return password
    except KeyboardInterrupt:
        return None