import abc
import logging
import pyodbc

from settings import MSSQL_PASSWORD, MSSQL_USER, MSSQL_HOST, MSSQL_DB, MSSQL_PORT, MSSQL_DRIVER
from data import LOOGING_LEVES


class DataSource(abc.ABC):
    api_connection = None
    driver = None
    source = None
    host = None
    port = None
    user = None
    password = None
    conn = None

    @abc.abstractmethod
    def connect(self, **kwargs):
        pass

    @abc.abstractmethod
    def close_conn(self, **kwargs):
        pass

    @abc.abstractmethod
    def get_data(self, **kwargs):
        pass


class MSSQLDataSource(DataSource):

    def __init__(self):
        self.api_connection = pyodbc
        self.driver = MSSQL_DRIVER
        self.source = MSSQL_DB
        self.host = MSSQL_HOST
        self.port = MSSQL_PORT
        self.user = MSSQL_USER
        self.password = MSSQL_PASSWORD

    def connect(self, **kwargs):
        logging.warning('Connecting to MSSQL database...')
        conn_params = 'DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}'.format(
                        self.driver,
                        self.host,
                        self.port,
                        self.source,
                        self.user,
                        self.password)
        self.conn = self.api_connection.connect(conn_params)

    def close_conn(self, **kwargs):
        self.conn.close()

    def get_data(self, **kwargs):
        table = kwargs.get('table')
        log_level = kwargs.get('log_level')
        logging.log(LOOGING_LEVES[log_level], "Getting data from table {} ...".format(table))
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM {};".format(table))
        data = cursor.fetchall()
        return data

