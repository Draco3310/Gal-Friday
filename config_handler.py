import configparser
config = configparser.ConfigParser()
config.read('settings.ini')
config_cache = None

def get_config():
    global config_cache
    if config_cache is None:
        config = configparser.ConfigParser()
        config.read('settings.ini')
        config_cache = config
    return config_cache
