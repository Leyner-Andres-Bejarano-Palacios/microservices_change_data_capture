import argparse

   

class ArgParser:
    MODULE_DESCRIPTION = "program for sending records to an event hubs topic"
    MODULE_VERSION = "1.0"
    MODULE_EPILOG = "Ultracom"
    PROPERTIES_PATH = "Path to properties file"
    @classmethod
    def fn_get_args(cls):
        parser = argparse.ArgumentParser(description = cls.MODULE_DESCRIPTION, \
            epilog = cls.MODULE_EPILOG)
        parser.add_argument('--properties-path', '-p', help = cls.PROPERTIES_PATH, \
            type = str, dest = 'vPropertiesPath', required = True)
        arguments = parser.parse_args()
        return arguments