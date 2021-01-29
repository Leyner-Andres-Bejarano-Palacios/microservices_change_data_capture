 #!/bin/sh 

 echo "Waiting for MSSQL SERVER..."

while ! nc -z $MSSQL_HOST $MSSQL_PORT; do
    sleep 0.1
done
echo "MSSQL SERVER started"

python /src/main.py