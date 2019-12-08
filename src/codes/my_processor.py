"""
my_processor.py - this module is for demonstration purpose only
"""


class MyProcessor:
    """
    MyProcessor - this class is for demonstration only
    """

    @staticmethod
    def run(df):
        return df.agg(['mean', 'min', 'max'])
