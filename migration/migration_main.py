from initialiser import *
from replicator import *
from migrator import * 

printTitle()
printAbility()
loading_spinner(15, "\033[PPlease wait\033[0m", "⠙")
#get_db_input_and_create_config()
print("Only REPLICATION supported as of now\n")
selectTable()
startMigration()






