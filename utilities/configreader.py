from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read(r'/home/vipulsai/PycharmProjects/Git_API_Automation/configurations/config.ini')
    return config.get(section, key)