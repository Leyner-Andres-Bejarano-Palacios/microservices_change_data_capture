from data_source import MSSQLDataSource


class DataSourceContext(object):
    strategy = None
    strategies = {
        'mssql': MSSQLDataSource,
        'oracle': ''
    }

    def get_data(self, strategy, **kwargs):
        self.strategy = self.strategies[strategy]()
        self.strategy.connect()
        data = self.strategy.get_data(**kwargs)
        self.strategy.close_conn()
        return data
