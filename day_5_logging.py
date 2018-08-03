import logging
import sys
# can also use logger which additionally allows for using log rotate

# this will log to console
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

# this logs to file
logging.basicConfig(filename="log.out", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

logging.DEBUG('hello world')