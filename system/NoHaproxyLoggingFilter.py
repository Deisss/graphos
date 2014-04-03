import logging

class NoHaproxyLoggingFilter(logging.Filter):
    ''' Disable haproxy logging filter '''
    def __init__(self, name='NoHaproxyLoggingFilter'):
        logging.Filter.__init__(self, name)

    def filter(self, record):
        return not record.getMessage().startswith('200 OPTIONS /checkhealth')