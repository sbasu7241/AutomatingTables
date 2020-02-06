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
CREATE USER 'frosty'@'localhost' IDENTIFIED BY 'some_pass';
```
Create database
```
CREATE DATABASE assignment;
```
Grant privileges for new user for this database
```
GRANT ALL PRIVILEGES ON shop.* TO 'frosty'@'localhost';
```
Log out root and log in as the new user
```
quit;
mysql -u frosty -p -h localhost
```
## Run python file
```
python fill.py
```


#### Open up the 'assignment' database as user 'frosty' in MySQL and viola the tables are there :)








