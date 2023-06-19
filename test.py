import make_db as db
from os import path

for i in range(0,len(db.tables)):
    print(db.table_names[i])
    for row in db.cursor.execute(f"select * from {db.table_names[i]}") :##this script will print all the information in your database to the console
        print ("\n",row)
    print("\n"+"\n")
