import logging
from logging import INFO

from data_context import DataSourceContext

if __name__ == '__main__':
    logging.basicConfig(level=INFO)
    log_level = 'INFO'
    table = 'cdc.dbo_info_CT'
    data_context = DataSourceContext()
    data = data_context.get_data(strategy='mssql', table=table, log_level=log_level)
    logging.info("Data retrieved: ")
    logging.info(data)