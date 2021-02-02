import configparser
from sender import Sender

class EventSenderBL:
    def __init__(self, vArgs):
        self._vArgs = vArgs
        self._vName = self.__class__.__name__
        self.__vProperties = self.fn_get_configs()
        self._sender = Sender(self.__vProperties)

    def fn_get_configs(self):
        configs = configparser.ConfigParser()
        with open(self._vArgs.vPropertiesPath, 'w') as configfile:
            configs.write(configfile)
        return configs

    def send(self,json_data):
        self.__sender.send(json_data)


