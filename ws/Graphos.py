import tornado.web, logging

from helper.PygalChart import PygalChart
from helper.PygalStyle import PygalStyle
from helper.PygalOptions import PygalOptions
from helper.PygalSeries import PygalSeries

class GraphosHandler(tornado.web.RequestHandler):
    ''' Main handler for generating graphs '''
    def exitAndClear(self, status):
        ''' Exit system '''
        self.clear()
        self.set_status(status)
        self.finish()

    def generate(self, name, style, options, series, output):
        ''' Render a new graph '''
        # Create a new factory and try to generate base graph
        chartGenerator = PygalChart(name)
        chart = chartGenerator.factory()

        if chart is None:
            logging.error('Chart could not be generated: %s' % name)
            self.exitAndClear(400)
            return None

        # Style
        styleGenerator = PygalStyle(chart)
        styleGenerator.setStyle(style)

        # Options
        optionsGenerator = PygalOptions()
        for key in options:
            optionsGenerator.clear()
            optionsGenerator.setChart(chart)
            optionsGenerator.append(key, options[key])

        # Series
        seriesGenerator = PygalSeries()
        for key in series:
            seriesGenerator.clear()
            seriesGenerator.setChart(chart)
            seriesGenerator.append(key, series[key])

        # Rendering
        if output == 'png':
            return chart.render_to_png()
        else:
            return chart.render()

    def getOption(self, option):
        ''' Get the option by it's name '''
        if option.startswith('options.'):
            return option[8:]
        elif option.startswith('option.'):
            return option[7:]
        elif option.startswith('o.'):
            return option[2:]
        else:
            return option[1:]

    def getSerie(self, serie):
        ''' Extracting series from their string literals '''
        separated = serie.split(':', 1)

        # Exactly two are needed
        if len(separated) != 2:
            logging.error('Serie could not be extracted: %s' % serie)
            self.exitAndClear(400)
            return None

        return {
            # The name
            'name': separated[0],
            # Separate into values
            'values': separated[1].split(',')
        }

    def defaultRequestParser(self):
        ''' Default render accessible threw get or post '''
        # required field
        name = self.get_argument('chart')
        style = self.get_argument('style', 'DefaultStyle', True)
        output = self.get_argument('output', 'svg', True)
        options = {}
        series = {}

        for key in self.request.arguments:
            # It's an options
            if key.startswith('o') and key != 'output':
                optionName = self.getOption(key)
                if optionName != '':
                    options[optionName] = self.get_argument(key, None)

            # It's a series options
            elif key.startswith('s') and key != 'style':
                serie = self.get_argument(key, None)
                if serie is not None:
                    extracted = self.getSerie(serie)
                    if extracted is not None:
                        series[extracted['name']] = extracted['values']
                    else:
                        return

        # Call for final rendering
        render = self.generate(name, style, options, series, output)
        if render is not None:
            # Specific output
            if output == 'png':
                self.set_header('Content-Type', 'image/png')
            elif output == 'svg':
                self.set_header('Content-Type', 'image/svg+xml')

            self.write(render)

    def get(self):
        ''' Get functionnality '''
        self.defaultRequestParser()

    def post(self):
        self.defaultRequestParser()