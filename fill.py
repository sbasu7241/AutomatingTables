import pandas as pd
from docx.api import Document
import mysql.connector


document = Document('table.docx')
table = document.tables[0]

data = []

keys = None

for i, row in enumerate(table.rows):
    text = (cell.text.encode('utf-8') for cell in row.cells)

    if i == 0:
        keys = tuple(text)
        continue
    row_data = tuple(text)
    data.append(row_data)
    
print (data)

print keys


mydb = mysql.connector.connect(
  host="localhost",
  user="francesco",
  passwd="some_pass",
  database="test"
)

cursor = mydb.cursor()

#sql_item ="CREATE TABLE Item_Table (item_id CHAR(20) NOT NULL,item_name CHAR(20) NOT NULL,Manu_name CHAR(20) NOT NULL,item_rate CHAR(20) NOT NULL,Sell_price CHAR(20) NOT NULL,item_description CHAR(20) NOT NULL)"


sql = "DROP TABLE IF EXISTS Item_Table"

cursor.execute(sql) 


sql_item ="CREATE TABLE Item_Table ("



for i in range(len(keys)):
	header = keys[i]
	repeat = str(header) + " CHAR(20) NOT NULL,"
	if i == (len(keys)-1):
		repeat = repeat = str(header) + " CHAR(20) NOT NULL)"
	sql_item += repeat

#print sql_item	

cursor.execute(sql_item)

#insert_sql = "INSERT INTO Depositor_Table (Customer_Name, Account_Number) VALUES (%s, %s)"

#insert_sql = "INSERT INTO Item_Table (item_id,item_name,Manu_name,item_rate,Sell_price,item_description) VALUES (%s, %s, %s, %s, %s, %s)"

insert_sql_header = "INSERT INTO Item_Table ("

sql_item = ""

for i in range(len(keys)):
	header = keys[i]
	repeat = str(header) + ","
	if i == (len(keys)-1):
		repeat = repeat = str(header)
	sql_item += repeat

sql_header = ") VALUES ("
sql_repeat = ""

if len(keys)==1:
	sql_repeat = "%s)"

else:
	for i in range(len(keys)-1):
		sql_repeat+="%s, "
	 
 	sql_repeat += "%s)"

insert_sql = insert_sql_header + sql_item + sql_header + sql_repeat 

print insert_sql



for i in range(len(keys)):
	val = data[i]
	cursor.execute(insert_sql, val)

#Deleting table for testing purporses

#cursor.execute("DROP TABLE Item_Table;")
		
mydb.commit()

print(cursor.rowcount, "record inserted.")



	
 


