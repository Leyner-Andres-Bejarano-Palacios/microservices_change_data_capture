/* TODO: Get database name from env */
USE testdb; 
GO

IF OBJECT_ID(N'testdb.dbo.info', N'U') IS NULL 
BEGIN 
CREATE TABLE testdb.dbo.info (
    id int NOT NULL IDENTITY PRIMARY KEY,
    value VARCHAR(50) NOT NULL,
);

EXECUTE sys.sp_cdc_enable_db;

EXEC sys.sp_cdc_enable_table 
@source_schema = N'dbo', 
@source_name   = N'info', 
@role_name     = NULL, 
@captured_column_list = '[id],[value]';
END; 
GO


PRINT 'Testing...'
PRINT 'Inserting data...'
INSERT into testdb.dbo.info values('Test Insert!');
GO

PRINT 'Getting data...'
WAITFOR DELAY '00:00:03';
SELECT * FROM cdc.dbo_info_CT;
GO