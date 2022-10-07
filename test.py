from make_db import cursor
from make_db import table_name
from os import path

for row in cursor.execute(f"select * from {table_name}") :##this script will print all the information in your database to the console
    print ("\n",row)

