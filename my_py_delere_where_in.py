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
            list_of_names = ['Jim', 'Bob']
            # Prepare the string with the same number of placeholders in
            # list_of_names
            format_strings = ','.join(['%s']*len(list_of_names))
            cursor.execute("DELETE from Friends WHERE name in ({});".format(format_strings), list_of_names)
            connection.commit()
        
finally:
    #Close the connection, regardsless of whether the above was successful
    connection.close()