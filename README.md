# Change Data Capture Template project 

## Set Up 

Execute the following commands to set up your local environment.

1. Build docker images for containers used.

```bash
docker-compose build 
```

Later on, we have to config our SQL server container.

2. Up database container.

```bash
docker-compose up -d db
```

3. Create the database to working with and activate Change Data Capture functionality:

```bash
docker exec -it db bash "./scripts/init_db.sh"
```

4. Up others services. 
```bash
docker-compose up 
```

That's all! Now, you can keep rocking in code with this project. 

## Testing 

If you want to see what there are in CDC table use the following command:

_Info_: You could find the password in .env file

```bash
docker exec -it db bash -c 'mssql-cli -U sa -P password -d testdb -Q "SELECT * FROM cdc.dbo_info_CT;"'
```