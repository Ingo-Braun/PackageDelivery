import logging
import os
import logging.handlers

def get_logger(name,dir=os.path.join("",'logs'),debug=True):
    
    if not os.path.exists(dir):
        os.makedirs(dir)

    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    return config(debug,log,dir,name)
    

def config(debug,log,dir,name):
    handler = logging.handlers.RotatingFileHandler(
            os.path.join(dir,'{}.log'.format(name)), mode='a', maxBytes=100000000, backupCount=5,encoding = "UTF-8")
    if debug:
        handler.setLevel(logging.DEBUG)
    else:
        handler.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s] [%(name)s %(funcName)s:%(lineno)d] %(levelname)s | %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log
