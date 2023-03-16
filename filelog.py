import logging

# Set up the logger
logging.basicConfig(filename='app.py', level=logging.DEBUG)

# Log a message at the DEBUG level
logging.debug('This is a debug message')

# Log a message at the INFO level
logging.info('This is an info message')

# Log a message at the WARNING level
logging.warning('This is a warning message')

# Log a message at the ERROR level
logging.error('This is an error message')

# Log a message at the CRITICAL level
logging.critical('This is a critical message')
