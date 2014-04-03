'''
PygalSeries helps to add series to a given chart
'''

class PygalSeries(object):
    ''' PygalSeries helps to add series to a given chart '''
    def __init__(self, chart=None, name=None, values=None):
        ''' Get the object and work with '''
        self.setChart(chart)
        self.setName(name)
        self.setValues(values)

    def clear(self):
        ''' Clear internal data stored '''
        self.chart = None
        self.name = None
        self.values = None

    def setChart(self, chart):
        ''' Set the chart to use '''
        if chart is not None:
            self.chart = chart

    def setName(self, name):
        ''' Set the serie name '''
        if (name is not None) and (isinstance(name, str) or 
                        isinstance(name, unicode)) and (name != ''):

            self.name = name

    def getName(self):
        ''' Get the serie name '''
        return self.name

    def setValues(self, values):
        ''' Set the serie values '''
        if (values is not None) and (isinstance(values, list)):
            parsed = []
            isFloat = False
            for val in values:
                try:
                    # Separate between float try and int try
                    if val.isdigit():
                        parsed.append(int(val))
                    else:
                        parsed.append(float(val))
                except ValueError:
                    pass
            self.values = parsed

    def getValues(self):
        ''' Get the serie values '''
        return self.values

    def isValid(self):
        ''' Check if everything is fine '''
        if self.chart is None:
            return False
        if self.name is None:
            return False
        if self.values is None:
            return False
        return True

    def append(self, name=None, values=None):
        ''' Append series to chart '''
        if name is not None:
            self.setName(name)
        if values is not None:
            self.setValues(values)

        if self.isValid():
            self.chart.add(self.getName(), self.getValues())
