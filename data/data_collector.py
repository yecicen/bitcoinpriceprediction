import bitmex
import coindesk
import coinmarketcap
import messari
import nomics

def getDataFromSource(source):
    if(source == "bitmex"):
        bitmex.run()
    elif(source == "coindesk"):
        coindesk.run()
    elif(source == "coinmarketcap"):
        coinmarketcap.run()
    elif(source == "messari"):
        messari.run()
    elif(source == "nomics"):
        nomics.run()
    else:
        raise Exception("Unknown data source")
        
def getDataFromAllSources():
    bitmex.run()
    coindesk.run()
    coindesk.run()
    coinmarketcap.run()
    messari.run()
    nomics.run()