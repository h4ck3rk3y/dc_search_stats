import logging

# create logger
lgr = logging.getLogger('logger_name')
lgr.setLevel(logging.DEBUG) # log all escalated at and above DEBUG

# add a file handler
fh = logging.FileHandler('dyna-anal.csv')

fh.setLevel(logging.DEBUG) # ensure all messages are logged to file

frmt = logging.Formatter('%(message)s;')
fh.setFormatter(frmt)

lgr.addHandler(fh)

def log(line, classification):
	lgr.info("%s"%(line.strip("\n") + "," + str(classification)))
