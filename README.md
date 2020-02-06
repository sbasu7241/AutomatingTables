# AutomatingTables
Automating my DBMS Home Work


## Installation
```
pip install --no-cache-dir -r requirements.txt
```
Note: 
1.  Keep the table.docx file in the same directory as the .py file
2.  Make sure SQL is installed on your system

## Configure your database
Login with root username
```
mysql -u root -p -h localhost
```
Create a new user with
```
CREATE USER 'francesco'@'localhost' IDENTIFIED BY 'some_pass';
```
Create database
```
CREATE DATABASE assignment;
```
Grant privileges for new user for this database
```
GRANT ALL PRIVILEGES ON shop.* TO 'francesco'@'localhost';
```
Log out root and log in as the new user
```
quit;
mysql -u francesco -p -h localhost
```
## Run python file
```
python fill.py
```


#### Open up the 'assignment' database in MySQL and viola the tables are there :)








