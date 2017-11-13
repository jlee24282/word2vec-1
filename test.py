import pandas as pd

"""
Data is from https://www.kaggle.com/sunnysai12345/news-summary/data
Kondalarao Vonteru
"""

class test(object):
    """
    Returning value in dictionary format
    """
    def __init__(datadir):
        data = {"topic": [], "summarized": [], "text": []}
        csvData             = pd.read_csv(datadir)
        data["summarized"]  = csvData["summarized"]
        data["text"]        = csvData["text"]
        data["topic"]        = csvData["headlines"]

    def getData(self):
        return self.data

