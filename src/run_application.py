"""
run_application.py - this is the main module to start the CherryPy service
"""

import cherrypy
import pandas as pd
from codes.my_processor import MyProcessor

p = MyProcessor()


class RunApplication(object):
    """
    RunApplication class contains codes to start CherryPy service
    """

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def process(self):
        """
        this process takes inputs from the service and returns output
        Returns
        -------

        """
        data = cherrypy.request.json
        df = pd.DataFrame(data)
        output = p.run(df)
        return output.to_json()


if __name__ == '__main__':
    config = {'server.socket_host': 'localhost',
              'server.socket_port': 4200}
    cherrypy.config.update(config)
    cherrypy.quickstart(RunApplication())
