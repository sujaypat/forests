from random import random

from bloombergobject import BloombergObject

class BBManager:

    everything = BloombergObject.Query.all()
    
    @staticmethod
    def update_tickerlist():
        BBManager.tickerlist = [x.Ticker for x in BBManager.everything.limit(1080)]

    def get_ticker_data(name=None):
        if name is None:
            possibilities = len(BBManager.tickerlist)
            n = int(possibilities * random())
            name = BBManager.tickerlist[n]
        return name, BBManager.everything.filter(Ticker=name)
