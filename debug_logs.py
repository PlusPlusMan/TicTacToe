import logging

def debug_logs():
    logging.basicConfig(filename="debug_logs.txt",
                        filemode='w',
                        #format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        format='%(asctime)s,%(msecs)d [%(levelname)s];\tin: %(filename)s, %(module)s, %(funcName)s, line=%(lineno)s;\tmsg= %(message)s',
                        encoding='utf-8',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
debug_logs()
