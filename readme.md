# Database Creator
This tool will help you create a SQLight database. This tool was created for Schreiner University's Intro to Databases class but is open and available to the public. To use this tool please clone this repo to your local machine or online editor and follow the instructions below.

---

## Before you get started

### Make sure you have git installed:

[Click here to install git for mac](https://git-scm.com/download/mac)

[Click here to install git for windows](https://git-scm.com/download/win)

[Click here to install git for Linux](https://git-scm.com/download/linux)

### Make sure you have Python installed:
[Python](https://www.python.org/)

### Either install a text editor or IDE onto your local machine or choose a web editor capable of interacting with git

#### Recommended local editors and IDEs:

[Visual Studio Code](https://code.visualstudio.com/)

[PyCharm](https://www.jetbrains.com/pycharm/)

#### Recommended web editors:

[Visual Studio Code Online](https://vscode.dev/)

[Replit](https://replit.com/)

### Be sure your editor is configured for Python:

[Setting up Python for Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial)

### Make sure you understand Tables and Schemas in SQL
I'm including documentation from SQLight's official page in case you need a refresher

[Schema Doc](https://www.sqlite.org/schematab.html)

[Table Doc](https://www.sqlite.org/lang_createtable.html)

---

## Editing the script

### Step Zero: Clone script

Either use the native features of your editor to clone this repository to your machine or web editor or navigate to the folder where you would like this script to reside on your machine before entering the following command into your terminal:

```bash
git clone https://github.com/JasonBoyett/SU_database_utility
```

If you do not know how to navigate in your terminal please refer to the following documentation:

[Windows](https://learn.microsoft.com/en-us/windows/terminal/)

[Mac](https://www.macworld.com/article/221277/command-line-navigating-files-folders-mac-terminal.html)

[Linux](https://www.pluralsight.com/guides/beginner-linux-navigation-manual)

### Step One: Provide a path for your Database

On line 10 of make_db.py you will find a string literal that should look like this:

```python
db_path = r"example.db"
```
change the contents of the string to the desired name of your database with .db at the end

```python
db_path = r"my_database.db"
```
If there is a specific location on your machine where you would like the database to be saved use the Path() method from pathlib to indicate the location where you would like the file to be created.

```python
db_path = Path("Documents/my_database.db")
```

For more info on the Path() method click [here](https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f#:~:text=You%20can%20use%20os.,on%20both%20Windows%20or%20Mac.)

### Step Two: Name Tables

On lines 37 - 40 I give an example of how I would define three different tables

```python
TABLE_ONE_NAME = "games"
TABLE_TWO_NAME = "orders"
TABLE_THREE_NAME = "customers"
table_names = (TABLE_ONE_NAME, TABLE_TWO_NAME, TABLE_THREE_NAME)
```
You could also define the names directly in the table_names tuple

```python
table_names = ("games", "orders", "customers")
```
The first way is considered best practice since you may have to re-use the names of the tables. But in the case of this script either option works the same.

If you want to add another table either create a new constant for it and add it to the table_names tuple

```python
TABLE_ONE_NAME = "games"
TABLE_TWO_NAME = "orders"
TABLE_THREE_NAME = "customers"
ADDED_TABLE_NAME = "added_table"
table_names = (TABLE_ONE_NAME, TABLE_TWO_NAME, TABLE_THREE_NAME, ADDED_TABLE_NAME)
```

Or you could define one more name in the table_names tuple

```python
table_names = ("games", "orders", "customers", "added_table")
```

### Step Three: Create Schema

On lines 48 - 72 I define the schema for the database. In each of the tuples I provide a name for each column of my tables and an associated data type and then add them to another tuple that holds all my table schemas

```python

table_one_schema = (
    "gameName text",
    "developer text", 
    "release_year integer"
)
table_two_schema = (
    "orderID text", 
    "customerID text",
    "gameName text",
    "priceInCents integer"
)
table_three_schema = (
    "customerID text",
    "firstName text", 
    "lastName text"
)

table_schemas = (
    schema_string_table_one,
    schema_string_table_two, 
    schema_string_table_three
)
```

Then on lines 78 - 87 I use a helper function to generate a SQL command to create the schemas and then I add them to a tuple

```python
schema_string_table_one = build_schema(table_names[0], schemas[0])
schema_string_table_two = build_schema(table_names[1], schemas[1])
schema_string_table_three = build_schema(table_names[2], schemas[2])

table_SQL_strings = (
    schema_string_table_one,
    schema_string_table_two,
    schema_string_table_three
)
```

To add another table you would define another table you would first make another schema and add it to table_schemas

```python

table_one_schema = (
    "gameName text",
    "developer text", 
    "releaseYear integer"
)
table_two_schema = (
    "orderID text", 
    "customerID text",
    "gameName text",
    "priceInCents integer"
)
table_three_schema = (
    "customerID text",
    "firstName text", 
    "lastName text"
)
added_table_schema = (
    "someData text",
    "someValue integer"
)

table_schemas = (
    schema_string_table_one,
    schema_string_table_two, 
    schema_string_table_three,
    added_table_schema
)
```
Then you would add another helper function 

```python
schema_string_table_one = build_schema(table_names[0], schemas[0])
schema_string_table_two = build_schema(table_names[1], schemas[1])
schema_string_table_three = build_schema(table_names[2], schemas[2])
schema_string_added = build_schema(table_names[3], schemas[3])

table_SQL_strings = (
    schema_string_table_one,
    schema_string_table_two,
    schema_string_table_three, 
    schema_string_added
)
```

### Step Four: Add data to tables

On lines 92 - 117 I add data to the tables. All you have to do here is fill the appropriate data for your database into the quotes and if you have more than three tables make a new tuple to represent it.

```python
table_one = (
    ("Minecraft", "Notch", 2011 ),
    ("Sekiro Shadows Die Twice", "From Software", 2019),
    ("Call of Duty 4", "Infinity Ward", 2007),
    ("Fortnight", "Epic Games", 2017),
    ("Dark Souls", "From Software", 2011)
)

table_two = (
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
```
To add an extra table simply make another tuple to represent it and then add it to the tables tuple

```python
table_one = (
    ("Minecraft", "Notch", 2011 ),
    ("Sekiro Shadows Die Twice", "From Software", 2019),
    ("Call of Duty 4", "Infinity Ward", 2007),
    ("Fortnight", "Epic Games", 2017),
    ("Dark Souls", "From Software", 2011)
)

table_two = (
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
added_table = (
    ("some data here")
)

tables = (
    table_one,
    table_two,
    table_three,
    added_table
)
```

Everything after this section is meant to feed the data into your new database and you shouldn't need to touch it.

---

# The Rick Roll means it worked 
