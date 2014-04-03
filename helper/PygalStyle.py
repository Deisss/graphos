'''
Detect and apply style to rendering graphics
'''

import pygal.style

class PygalStyle(object):
    ''' Detect and apply style to rendering graphics '''
    def __init__(self, chart=None, style=None):
        ''' Get the object and work with '''
        self.setChart(chart)
        self.setStyle(style)

    def setChart(self, chart):
        ''' Set the chart to use '''
        if chart is not None:
            self.chart = chart

    def setStyle(self, style):
        ''' Set the style to use '''
        if self.chart is not None:
            if style == 'BlueStyle':
                self.chart.config.style = pygal.style.BlueStyle
            elif style == 'CleanStyle':
                self.chart.config.style = pygal.style.CleanStyle
            elif style == 'DarkColorizedStyle':
                self.chart.config.style = pygal.style.DarkColorizedStyle
            elif style == 'DarkGreenBlueStyle':
                self.chart.config.style = pygal.style.DarkGreenBlueStyle
            elif style == 'DarkGreenStyle':
                self.chart.config.style = pygal.style.DarkGreenStyle
            elif style == 'DarkSolarizedStyle':
                self.chart.config.style = pygal.style.DarkSolarizedStyle
            elif style == 'DarkenStyle':
                self.chart.config.style = pygal.style.DarkenStyle
            elif style == 'DefaultStyle':
                self.chart.config.style = pygal.style.DefaultStyle
            elif style == 'DesaturateStyle':
                self.chart.config.style = pygal.style.DesaturateStyle
            elif style == 'LightColorizedStyle':
                self.chart.config.style = pygal.style.LightColorizedStyle
            elif style == 'LightGreenStyle':
                self.chart.config.style = pygal.style.LightGreenStyle
            elif style == 'LightSolarizedStyle':
                self.chart.config.style = pygal.style.LightSolarizedStyle
            elif style == 'LightStyle':
                self.chart.config.style = pygal.style.LightStyle
            elif style == 'LightenStyle':
                self.chart.config.style = pygal.style.LightenStyle
            elif style == 'NeonStyle':
                self.chart.config.style = pygal.style.NeonStyle
            elif style == 'RedBlueStyle':
                self.chart.config.style = pygal.style.RedBlueStyle
            elif style == 'RotateStyle':
                self.chart.config.style = pygal.style.RotateStyle
            elif style == 'SaturateStyle':
                self.chart.config.style = pygal.style.SaturateStyle
            elif style == 'SolidColorStyle':
                self.chart.config.style = pygal.style.SolidColorStyle
            elif style == 'Style':
                self.chart.config.style = pygal.style.Style
            elif style == 'TurquoiseStyle':
                self.chart.config.style = pygal.style.TurquoiseStyle