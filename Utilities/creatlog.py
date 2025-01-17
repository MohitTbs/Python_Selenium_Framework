import logging
import os.path
import sys
from Utilities.util import get_root_of_project


def loggen():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler(filename=os.path.join(get_root_of_project(), "logfile.log"), mode='w')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)
    return logger
