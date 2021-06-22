import asyncio, websockets, threading, time, sys
from datetime import datetime, date, timedelta
from collections import namedtuple
from os import system
from json import dumps as jsenc
from json import loads as jsdec
from pickle import dump
import csv
import constants

errorCount = 0
data = {}
# websocket_url = "wss://www.bitmex.com/realtime?subscribe=orderBook10:XBTUSD"
# subTopic = "orderBook10:XBTUSD"
system('title ' + constants.BITMEX_WEBSOCKET_URL + " channel:" + constants.BITMEX_SUB_TOPIC)

async def runWS():
    async with websockets.connect(constants.BITMEX_WEBSOCKET_URL) as websocket:
        global gCount
        global data
        start =datetime.now().time()
        yesterdate = date.today()
        header_added = False
        while True:
            tickerEnc = await websocket.recv()
            tickerEnc = jsdec(tickerEnc)
            data=str(tickerEnc)
            if data[0:4]=="{'ta":
                a = (data.split("'asks': [["))[1]
                b = a.split(", ")
                askprice=float(b[0])
                c=b[1].split("]")
                askvol=float(c[0])
                askvol2=float(b[3].split("]")[0])
                askvol3=float(b[5].split("]")[0])
                askvol4=float(b[7].split("]")[0])
                askvol5=float(b[9].split("]")[0])
                d = (data.split("'bids': [["))[1]
                e = d.split(", ")
                bidprice=float(e[0])
                f=e[1].split("]")
                bidvol=float(f[0])
                bidvol2=float(e[3].split("]")[0])
                bidvol3=float(e[5].split("]")[0])
                bidvol4=float(e[7].split("]")[0])
                bidvol5=float(e[9].split("]")[0])
                totalaskvol=askvol*5+askvol2*4+askvol3*3+askvol4*2+askvol5*1
                totalbidvol=bidvol*5+bidvol2*4+bidvol3*3+bidvol4*2+bidvol5*1
                midprice=(askprice+bidprice)/2
                fee=(midprice*0.001+0.5)/2
                superprice=midprice-fee+(totalbidvol/(totalbidvol+totalaskvol))*fee*2
                g = (data.split("'timestamp': '"))[1]
                h = g.split("'")
                rightnow = datetime.now().time()
                sec = timedelta(hours=0, minutes=0, seconds=2)
                if(datetime.combine(date.today(), rightnow)-datetime.combine(yesterdate, start))>sec:
                    start=datetime.now().time()
                    yesterdate=date.today()
                    #you can save the information to file
                    with open('bitmex.csv', mode='a') as csv_file:
                        fieldnames = ['timestamp', 'askprice', 'bidprice', 'superprice']
                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        if not header_added:
                            writer.writeheader()
                            header_added = True
                        writer.writerow(
                            {
                                'timestamp': rightnow,
                                'askprice': askprice, 
                                'bidprice': bidprice,
                                'superprice': superprice,
                            })
def run():
    try:
        asyncio.get_event_loop().run_until_complete(runWS())
        time.sleep(60.0)
    except Exception as e:
        global x
        x=e
        print(e)
        global errorCount
        errorCount +=1
        print("Error in websocket, retrying, attempt #" + str(errorCount) + "\n" + str(type(e)) + "\t" +str(e))
        time.sleep(60.0)
        run()

