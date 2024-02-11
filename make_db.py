# This script is heavily commented to make it easier for a student to use. If you have any problems please contact the professor of one of the TAs for assistance.
# Please read all comments and readme before editing this script and if you do not understand what something does or how to adapt it for your use case please contact the professor or a TA

# import statements let the program have access to functionality that it doesn't always have.
import sqlite3 as sql # the "as" command in python renames the import so it can be called by whatever name the programer choses
from pathlib import Path
from sre_constants import SUCCESS # this path utility might be necessary for the student to make sure their database is saved in the proper location but it is not currently in use
from  util import build_complete 

#this is a helper function that for defining your schema
def build_schema(table_name, schema_tuple):
    schema_string = f"create table {table_name} "
    for i in range(0, len(schema_tuple)):
        if i == 0:
            schema_string += f"({schema_tuple[i]}"
        elif i == len(schema_tuple) - 1:
            schema_string += f", {schema_tuple[i]})"
        else:
            schema_string += f", {schema_tuple[i]}"
    return schema_string

##################STEP ONE: PROVIDE THE PATH FOR DATABASE#################

db_path = r"example.db" # put the path to your database followed by /name-of-database.db in this string for example C:/test-folder/example.db
#the lower case r next to this string turns it into a string literal which means it will ignore escape characters. So, no need for double backslashes or anything of that nature

# creates a connection to the database and creates the database if it does not already exist
connection = sql.Connection(db_path)

#the cursor object is used to send commands to your database
cursor = connection.cursor()

##################STEP TWO: NAME TABLES#################

# I'm using a video game ordering service for the example database so the tables will be for the games that I sell, orders placed and my customers
# these are the names of the tables in the database. The words on the right of the equals sign are the name of the variable and the words in quotes on the left of the equals sign are what that variable represents.
TABLE_ONE_NAME = "games" # name of the table you wish to create
TABLE_TWO_NAME = "orders" # since the names of the tables are constants they are all capitalized and separated by underscores
TABLE_THREE_NAME = "customer"
table_names = (TABLE_ONE_NAME, TABLE_TWO_NAME, TABLE_THREE_NAME) #put the names of all of your tables in this tuple. 
# You can either type them out in quotes or declare them as constants like I did above. it is considered best practice to declare them as constants

##################STEP THREE: CREATE SCHEMA#################

# here you create tuples that contain the schema for your tables
# the first word in each element of the schema list is the name of the table element
# the second word in each of the elements of your schema list is the data type held by that field
table_one_schema = (
    "gameName text",
    "developer text",
    "releaseYear integer"
) 
# the naming convention for your table names is that all words are lower case and that words are separated by an underscore.
table_two_schema = (
    "orderID text",
    "customerID text",
    "gameName text",
    "priceInCents integer"
)
# each table will have its own schema
table_three_schema = (
    "customerID text",
    "firstName text",
    "lastName text"
)
# remember to keep the names of the variables that hold your tables and their corresponding tables consistent

schemas = (
    table_one_schema,
    table_two_schema, 
    table_three_schema
) # this is a tuple that holds all of your schemas if you want to add another table make sure to add its schema to this list

# here I use a helper function to build the schema strings for each of the tables
# if you want to add another table you will need to add another schema strings
# you can do so by naming the schema string and setting it equal to the build_schema function
# and passing it the name of the table and the schema for that table
schema_string_table_one = build_schema(table_names[0], schemas[0])
schema_string_table_two = build_schema(table_names[1], schemas[1])
schema_string_table_three = build_schema(table_names[2], schemas[2])

# a list to store all of the schemas
table_SQL_strings = (
    schema_string_table_one,
    schema_string_table_two,
    schema_string_table_three
)

##################STEP FOUR: ADD DATA TO TABLES#################

#this is where you will set up the data to be stored in your database
table_one = (# this is a tuple, tuples are immutable and can be passed as an argument in sqlite to create or edit a table
    ("Minecraft", "Notch", 2011 ),
    ("Sekiro Shadows Die Twice", "From Software", 2019),
    ("Call of Duty 4", "Infinity Ward", 2007),
    ("Fortnight", "Epic Games", 2017),
    ("Dark Souls", "From Software", 2011)
)

table_two = (# remember to keep track of which table is which and its corresponding name, schema and elements
    ("Example Order", "1234JD", "Call of Duty 4", "2998"),
    ("Example Order 2", "4321jd", "Sekiro", "4499"),
    ("Example Order 3", "1234JD", "Fortnight", "1299"),
    ("Example Order 4", "135JB", "Dark Souls", "1599")
)

table_three = (
    ("1234JD", "John", "Doe"),
    ("4321jd", "Jane", "Doe"),
    ("135JB", "Jim", "Bob")
)

tables = (
    table_one,
    table_two,
    table_three
)


if __name__ == '__main__':#this is the code that will execute when you run the program. There is no reason to change anything after this point.

    for i in range(0,len(table_SQL_strings)): # this loops through your schemas and uses them to create new tables in your database
        cursor.execute(table_SQL_strings[i]) # this command creates the individual tables 
    
    for i in range(0,len(table_names)): # this takes the values you put into your tables and adds their values into the database table
        insert = (("?, ")*len(tables[i][0])) # in order to populate the tables with data there needs to be a number of question marks 
        insert = insert[:-2]
        cursor.executemany(f"insert into {table_names[i]} values ({insert})", tables[i])

    # build_complete.confirm()
    #saves your database
    connection.commit()