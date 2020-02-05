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
    row_data = dict(zip(keys, text))
    data.append(row_data)
    
print (data)

df = pd.DataFrame(data)

#print(df.columns.values)


mydb = mysql.connector.connect(
  host="localhost",
  user="francesco",
  passwd="some_pass",
  database="test"
)

cursor = mydb.cursor()

sql_depositor ="CREATE TABLE Depositor_Table (Customer_Name CHAR(20) NOT NULL,Account_number CHAR(20) NOT NULL)"

cursor.execute(sql_depositor)

insert_sql = "INSERT INTO Depositor_Table (Customer_Name, Account_Number) VALUES (%s, %s)"

for i in range(len(df)):
	val = tuple(df.iloc[i].values)
	cursor.execute(insert_sql, val)

#Deleting table for testing purporses

cursor.execute("DROP TABLE Depositor_Table;")
		
mydb.commit()

print(cursor.rowcount, "record inserted.")



	
 



