## Steps Taken:

### Start mysql
``` mysql-ctl start ```

### Login
``` mysql -u $C9_USER -p ```

### Install pymysql
``` sudo pip3 install pymysql ```

### Grab the shinook dummy database from git
``` wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_MySql_AutoIncrementPKs.sql ```

### Import the database
``` mysql -u $C9_USER -p < Chinook_MySql_AutoIncrementPKs.sql ```

### Import the requirements into text file
``` pip3 freeze > requirements.txt ```