# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:20:02 2021

@author: divyp
"""
import csv

def createcsv(filename):
    with open(f"logs/{filename}.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        heading = ["Timestamp","Currency Pair","Change Status","Tweet status"]
        wr.writerow(heading)
    
def logtocsv(filename,timestamp, currencypair, tweet):
    with open(f"logs/{filename}.csv", 'a', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        if tweet == "No change":
            csvline = [timestamp, currencypair, tweet, "No tweet"]
            wr.writerow(csvline)
        elif tweet == "Something went wrong":
            csvline = [timestamp, currencypair, "ERROR", "ERROR"]
            wr.writerow(csvline)
        else:
            csvline = [timestamp, currencypair, "Change Detected", "Tweeted"]
            wr.writerow(csvline)