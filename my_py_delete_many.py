import os
import pymysql

#Get username from Cloud9 workspace
#Modify this if running on another environment
username = os.getenv('C9_USER')

#Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
                            
try:
    #Run a query
    with connection.cursor() as cursor:
        rows = cursor.executemany("DELETE from Friends WHERE name = %s;", ['Bob', 'Fred'])
        connection.commit()
finally:
    #Close the connection, regardsless of whether the above was successful
    connection.close()