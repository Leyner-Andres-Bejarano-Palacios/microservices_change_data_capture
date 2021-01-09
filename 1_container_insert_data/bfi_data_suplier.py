import uuid
import pyodbc
import datetime


server = 'db'
database = 'testdb'
username = 'SA'
password = '1Secure*Password1'   
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+\
                    ';SERVER='+server+\
                    ';PORT=1433;DATABASE='+database+\
                    ';UID='+username+\
                    ';PWD='+ password) as conn:
       with conn.cursor() as cursor:
        cursor.execute("insert into testdb.dbo.info(value) values (?)",(str(uuid.uuid4())))      
        cursor.commit()
