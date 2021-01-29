# DB settings 
import os 

# MSSQL config 
MSSQL_HOST = os.getenv('MSSQL_HOST', 'db')
MSSQL_PASSWORD = os.getenv('SA_PASSWORD')
MSSQL_DB = os.getenv('MSSQL_DB')
MSSQL_PORT = os.getenv('MSSQL_PORT', 1433)
MSSQL_USER = os.getenv('MSSQL_USER', 'SA')
MSSQL_DRIVER = '{FreeTDS}'
