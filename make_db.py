import sqlite3 as sql #the as command in python renames the import so it can be called by whatever name the programer choses
from os import path

db_path = r"example.db" #put the path to your database followed by /name-of-database.db in this string for example C:/test-folder/example.db
#for example Computer/user/exampleUser/Documents/db_Folder/games.db
#creates a connection to the database and creates the database if it does not already exist
connection = sql.Connection(db_path)
#the cursor object is used to send commands to your database
cursor = connection.cursor()
TABLE_ONE_NAME = "games"#name of the table you wish to create
TABLE_TWO_NAME = "orders"
TABLE_THREE_NAME = "customer"
table_names = (TABLE_ONE_NAME, TABLE_TWO_NAME, TABLE_THREE_NAME)


table_one_schema = ("gameName text", "developer text", "release_year integer") #the naming convention for your table names is that all words are lower case and that words are separated by an underscore.
#the second word in each of the pieces of your schema topple is the data type held by that field
table_two_schema = ("orderID text", "customerID text", "gameName text", "priceInCents integer")
table_three_schema = ("customerID text", "firstName text", "lastName text")

#this is a formatted string that will be used to create your database
schema_string_table_one = f"create table {TABLE_ONE_NAME} ({table_one_schema[0]} , {table_one_schema[1]} , {table_one_schema[2]})"#each element of your schema should be called here inside brackets and separated by commas. If you have more than three elements simply add more elements following the same patter 
schema_string_table_two = f"create table {TABLE_TWO_NAME} ({table_two_schema[0]}, {table_two_schema[1]}, {table_two_schema[2]}, {table_two_schema[3]})"
schema_string_table_three = f"create table {TABLE_THREE_NAME} ({table_three_schema[0]}, {table_three_schema[1]}, {table_three_schema[2]})"

table_schemas = (schema_string_table_one, schema_string_table_two, schema_string_table_three)

table_one = [#this is a tuple, tuples are immutable and can be passed as an argument in sqlite to create or edit a table
    #I'm using an example of video games for this database but you will edit this topple to fit your particular database
    ("Minecraft", "Notch", 2011 ),
    ("Sekiro Shadows Die Twice", "From Software", 2019),
    ("Call of Duty 4", "Infinity Ward", 2007),
    ("Fortnight", "Epic Games", 2017),
    ("Dark Souls", "From Software", 2011)
]

table_two = [
    ("Example Order", "1234JD", "Call of Duty 4", "2998"),
    ("Example Order 2", "4321jd", "Sekiro", "4499"),
    ("Example Order 3", "1234JD", "Fortnight", "1299"),
    ("Example Order 4", "135JB", "Dark Souls", "1599")
]

table_three = [
    ("1234JD", "John", "Doe"),
    ("4321jd", "Jane", "Doe"),
    ("135JB", "Jim", "Bob")
]

tables = [(table_one), (table_two), (table_three)]


if __name__ == '__main__':#ignore this it's here for testing reasons

    #this takes your schema and uses it to create a new table in your database.
    for i in range(0,len(table_schemas)):
        cursor.execute(table_schemas[i])
    #this takes the values you put into your tables and adds their values into the database table
    for i in range(0,len(table_names)):
        insert = (("?, ")*len(tables[i][i]))
        insert = insert[:-2]
        cursor.executemany(f"insert into {table_names[i]} values ({insert})", tables[i])
    #saves your database
    connection.commit()