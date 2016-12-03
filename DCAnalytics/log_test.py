import logging

# create logger
lgr = logging.getLogger('logger_name')
lgr.setLevel(logging.DEBUG) # log all escalated at and above DEBUG

# add a file handler
fh = logging.FileHandler('log.csv')
fh.setLevel(logging.DEBUG) # ensure all messages are logged to file

frmt = logging.Formatter('%(asctime)s,%(message)s')
fh.setFormatter(frmt)

lgr.addHandler(fh)

def log(ip_add, query):
	lgr.debug("%s:%s"%(ip_add, query))