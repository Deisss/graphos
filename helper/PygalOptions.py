'''
PygalOptions helps to add options to rendering graphs
'''

# Options which should be converted into boolean
boolconv = [
    'disable_xml_declaration',
    'explicit_size',
    'fill',
    'human_readable',
    'include_x_axis',
    'legend_at_bottom',
    'logarithmic',
    'no_prefix',
    'pretty_print',
    'print_values',
    'print_zeroes',
    'show_dots',
    'show_legend',
    'show_minor_x_labels',
    'show_minor_y_labels',
    'show_x_guides',
    'show_y_guides',
    'show_y_labels',
    'stroke'
]
# Options which should be converted into integer
intconv = [
    'dots_size',
    'height',
    'inner_radius',
    'interpolation_precision',
    'label_font_size',
    'legend_box_size',
    'legend_font_size',
    'major_label_font_size',
    'margin',
    'no_data_font_size',
    'order_min',
    'rounded_bars',
    'spacing',
    'title_font_size',
    'tooltip_border_radius',
    'tooltip_font_size',
    'truncate_label',
    'truncate_legend',
    'value_font_size',
    'width',
    'x_label_rotation',
    'x_labels_major_count',
    'x_labels_major_every',
    'y_label_rotation',
    'y_labels_major_count',
    'y_labels_major_every'
]
# Options which should be converted into float
floatconv = [
    'x_scale',
    'y_scale',
    'zero'
]
# Options which contains list element
listconv = [
    'x_labels_major',
    'y_labels_major'
]
# Integer/float which allows negative values (all of them can be negative)
negconv = [
    'order_min',
    'x_label_rotation',
    'y_label_rotation',
    'x_scale',
    'y_scale',
    'zero'
]







class PygalOptions(object):
    ''' PygalOptions helps to add options to rendering graphs '''
    def __init__(self, chart=None, name=None, value=None):
        self.clear()
        self.setChart(chart)
        self.setName(name)
        self.setValue(value)


    def clear(self):
        ''' Clear internal data stored '''
        self.chart = None
        self.name = None
        self.value = None
        self.converter = None

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

    def setValue(self, value):
        ''' Set the config value '''
        if (value is not None) and (isinstance(value, str) or
                            isinstance(value, unicode)) and(value != ''):
            self.value = value

    def getValue(self):
        ''' Get the config value '''
        return self.value

    def isValid(self):
        ''' Check if everything is fine '''
        if self.chart is None:
            return False
        if self.name is None:
            return False
        # We disallow using '_' (private/protected properties)
        if self.name.startswith('_'):
            return False
        if self.value is None:
            return False
        return True

    def __convBool(self, b):
        ''' Simple string to boolean convertion '''
        if b == True or b == '1' or b == 1 or b == 'true' or b == 'True' or b == 'yes' or b == 'Yes':
            return True
        else:
            return False

    def __convInt(self, i):
        ''' Simple String to integer convertion '''
        try:
            return int(i)
        except ValueError:
            return 0

    def __convFloat(self, f):
        ''' Simple String to float convertion '''
        try:
            return float(f)
        except ValueError:
            return 0.0

    def __convList(self, l):
        ''' Simple String to List convertion '''
        return l.split(',')

    def __convTuple(self, t):
        ''' Simple String to tuple convertion '''
        return tuple(self.__convList(t))

    def append(self, name=None, value=None):
        ''' Append the given option to the chart '''
        if name is not None:
            self.setName(name)
        if value is not None:
            self.setValue(value)

        if self.isValid():
            # Try to apply the converter before rendering
            name = self.getName()
            value = self.getValue()

            # 'normal' case
            if name in boolconv:
                value = self.__convBool(value)
            elif name in intconv:
                value = self.__convInt(value)
            elif name in floatconv:
                value = self.__convFloat(value)
            elif name in listconv:
                value = self.__convList(value)

            # Specific case
            elif name == 'interpolate':
                if value in ['cubic', 'quadratic',
                        'lagrange', 'trigonometric', 'hermite']:
                    pass
                else:
                    value = 'cubic'
            elif name == 'range':
                value = self.__convTuple(value)
            elif name in ['x_labels', 'y_labels']:
                # can be both tuple or string
                # Tuple
                if ',' in value:
                    value = self.__convTuple(value)
                # String, keep it like this...
                else:
                    pass
            # Some parameter (like title) are string, so we keep them
            else:
                pass

            try:
                setattr(self.chart.config, name, value)
            except AttributeError:
                pass
