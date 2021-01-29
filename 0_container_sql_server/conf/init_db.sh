 #!/bin/bash 

 echo "Waiting for MSSQL SERVER..."

while ! nc -z localhost 1433; do
    sleep 0.1
done
echo "MSSQL SERVER started"
sleep 1
/opt/mssql-tools/bin/sqlcmd -U sa -P $MSSQL_PASSWORD -v DBName=$MSSQL_DB -i /scripts/create_db.sql
/opt/mssql-tools/bin/sqlcmd -U sa -P $MSSQL_PASSWORD -v DBName=$MSSQL_DB -i /scripts/activate_cdc.sql