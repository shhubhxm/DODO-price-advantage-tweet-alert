# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:03:11 2021

@author: divyp
"""
from datetime import datetime
import GetDodoAdvantage as GDA
import bot_log as log
import twitter_bot as TB
import time

advantageThreshold = 0

currencyPairs = ['WETH-USDC',
                     'LINK-USDC',
                     'AAVE-USDC',
                     'SNX-USDC',
                     'COMP-USDC',
                     'WBTC-USDC',
                     'YFI-USDC',
                     'USDT-USDC']

print("Bot has been started")
dt_string = datetime.now().strftime("%d.%m.%Y %H_%M_%S")
filename = f"Twitter log {dt_string}"
file = log.createcsv(filename)
flag = True

try:
    while flag:
        # time.sleep(0.9)
        x = GDA.queryAllPricesDodoAndChainlink()
        for each in currencyPairs :
            currencyPair = each
            percentage = x[each]["dodopriceedgepercentage"]
            chainlinkPrice = x[each]["chainlinkPrice"]
            dodoPrice = x[each]["dodoPrice"]
            chainlinktimestamp = x[each]['chainlinkTimestamp']
            chainlinktimestamp = datetime.fromtimestamp(chainlinktimestamp)
            if percentage>advantageThreshold:
            # if True:
                    try:
                        time.sleep(0.01)
                        tweetText = TB.postPriceEdge(currencyPair, percentage, chainlinkPrice, dodoPrice, chainlinktimestamp)
                        log.logtocsv(filename, datetime.now(), each, "")
                        # print(f"{currencyPair} TWEET SUCCESFULL")
                    except Exception as err:
                        e = str(err)
                        if e == "[{'code': 187, 'message': 'Status is a duplicate.'}]":
                            # print("DUPLICATE TWEET")
                            # log.logtocsv(filename, datetime.now(),each,"No change")
                            pass
                        else:
                            print('ERROR WHILE TRYING TO TWEET')
                            log.logtocsv(filename, datetime.now(),each,"Something went wrong")
                            print(err)
except KeyboardInterrupt:
    print("Bot has been stopped")
    pass