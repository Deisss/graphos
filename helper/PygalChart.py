'''
PygalChart is a helper to convert a string chart name
into object instance from pygal
'''

import pygal, logging

class PygalChart(object):
    ''' Detect and check the pygal type '''

    def __init__(self, name=None):
        ''' Check if the name submitted is valid pygal or not '''
        self.name = None
        self.setName(name)

    def getName(self):
        ''' Get the stored name '''
        return self.name

    def setName(self, name):
        ''' Set the pygal name '''
        if (name is not None) and (isinstance(name, str) or
                            isinstance(name, unicode)) and (name != ''):

            self.name = name

    def isValid(self):
        ''' Check if valid is valid or not '''
        if (self.name is not None) and (self.name in pygal.CHARTS_BY_NAME):
            return True
        else:
            return False

    def factory(self):
        ''' Get the class ready from the name given '''
        if self.isValid():
            chart = pygal.CHARTS_BY_NAME[self.name]
            return chart()
        else:
            return None
