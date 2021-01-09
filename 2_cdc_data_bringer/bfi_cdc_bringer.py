import json
import uuid
import pyodbc
import requests
import datetime
import decimal

def dec_serializer(o):
    if isinstance(o, decimal.Decimal):
        return float(o)
    else:
        return str(o)

# def divide(o):
#     print 'entering divide'
#     result = 0
#     try:
#         string_version = str(o)
#         return 
#     except:
#         print 'error'
#     else:
#         print 'no error'
#     finally:
        # print 'exit'

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
        cursor.execute("SELECT * FROM cdc.dbo_info_CT")
        rows = cursor.fetchall()
        for row in rows:
            data = json.dumps(row, default=dec_serializer)
            print(type(data))
            print(dir(row))
            print(data)
            headers = {'content-type': 'application/json'}
            r = requests.post("http://conne_python_sender:5000/", data=data, headers=headers)
            print(r.text)


