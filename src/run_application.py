"""
run_application.py - this is the main module to start the CherryPy service

contains:
class - RunApplication
"""

import cherrypy
import pandas as pd
from codes.my_processor import MyProcessor

p = MyProcessor()


class RunApplication(object):
    """
    RunApplication class contains codes to start CherryPy service

    contains:
    function - process
    """

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def process(self):
        """
        takes inputs from the service and returns output

        Returns (json)
        -------
        result of function run in json format
        """
        data = cherrypy.request.json
        df = pd.DataFrame(data)
        output = p.run(df)
        print(output)
        return output.to_json()


if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0',
              'server.socket_port': 8080}
    cherrypy.config.update(config)
    cherrypy.quickstart(RunApplication())
