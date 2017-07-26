import logging
import logging.config
from pypacker.layer12 import cope
import time
import timeit
# import COPE_packet_classes as COPE_classes
logging.config.fileConfig('logging.conf')

class LoggerTest(object):

    def __init__(self):
        self.logger =logging.getLogger('nc_node.LoggerTest')

    def doSomething(self):
        self.logger.debug("Hello World!")
        pass

def main():
    loggertest = LoggerTest()
    iter_count = 10000
    print(timeit.timeit("loggertest.doSomething()", setup="from __main__ import LoggerTest; loggertest=LoggerTest()", number=iter_count) / iter_count * 1000)

if __name__ == '__main__':
    main()