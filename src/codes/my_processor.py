"""
my_processor.py - this module is for demonstration purpose only

contains classes:
MyProcessor
"""


class MyProcessor:
    """
    MyProcessor - this class is for demonstration only

    contains:
    static method: run
    """

    @staticmethod
    def run(df):
        """
        ::function : run :: calculates numerical aggregates

        Parameters
        ----------
        df (pandas DataFrame): data frame containing numerical columns

        Returns
        -------
        (pandas DataFrame): returns mean, min and max of the numerical columns
        """
        return df.agg(['mean', 'min', 'max'])
