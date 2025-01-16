import os
import sys
from configparser import ConfigParser
from Utilities.util import get_root_of_project


def read_configuration(category, key):
    config = ConfigParser()
    config.read(os.path.join(get_root_of_project(), 'Configurations', 'config.ini'))
    return config.get(category, key)
