import sqlite3 as sql #the as command in python renames the import so it can be called by whatever name the programer choses
from os import path

db_path = r"example.db" #put the path to your database followed by /name-of-database.db in this string for example C:/test-folder/example.db
#for example Computer/user/exampleUser/Documents/db_Folder/games.db
#creates a connection to the database and creates the database if it does not already exist
connection = sql.Connection(db_path)
#the cursor object is used to send commands to your database
cursor = connection.cursor()
table_name = "games"#name of the table you wish to create

if __name__ == '__main__':#ignore this it's here for testing reasons

    db_schema = ("name text", "developer text", "release_year integer") #the naming convention for your table names is that all words are lower case and that words are seperated by an underscore.
    #the second word in each of the pieces of your schema topple is the data type held by that field


    table = [#this is a tuple, topples are immutable and can be passed as an argument in sqlite to create or edit a table
        #I'm using an example of video games for this database but you will edit this topple to fit your particular database
        ("Minecraft", "Notch", 2011 ),
        ("Sekiro Shadows Die Twice", "From Software", 2019),
        ("Call of Duty 4", "Infinity Ward", 2007),
        ("Fortnight", "Epic Games", 2017),
        ("Dark Souls", "From Software", 2011)
    ]
    #this is a formatted string that will be used to create your database
    schema_string = f"create table {table_name} ({db_schema[0]} , {db_schema[1]} , {db_schema[2]})"#each element of your schema should be called here inside brackets and seperated by commas. If you have more than three elements simply add more elements following the same patter 

    #this takes your schema and uses it to create a new table in your database.
    cursor.execute(schema_string)
    #this takes the values you put into your tables and adds their values into the database table
    cursor.executemany(f"insert into {table_name} values (?,?,?)", table)#the number of question marks here should correspond to the number of elements in your table
    #saves your database
    connection.commit()