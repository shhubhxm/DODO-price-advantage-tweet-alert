# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 00:27:39 2021

@author: divyp
"""

import tweepy
import json

with open('Twitter.json','r') as file:
        TWITTER_CREDENTIALS = json.load(file)

auth = tweepy.OAuthHandler(TWITTER_CREDENTIALS[0]["consumer_key"], TWITTER_CREDENTIALS[0]["consumer_secret"])
auth.set_access_token(TWITTER_CREDENTIALS[0]["access_token"], TWITTER_CREDENTIALS[0]["access_token_secret"])
api = tweepy.API(auth)

dictionary = {
              "WETH-USDC":"Wrapped ETH - U.S. dollar coin",
              "LINK-USDC":"LINK - U.S. dollar coin",
              "AAVE-USDC":"ETHLend - U.S. dollar coin",
              "SNX-USDC":"Synthetix Network Token - U.S. dollar coin",
              "COMP-USDC":"Compound Cryptocurrency - U.S. dollar coin",
              "WBTC-USDC":"Wrapped Bitcoin - U.S. dollar coin",
              "YFI-USDC":"Yearn Finance - U.S. dollar coin",
              "USDT-USDC":"Tether - U.S. dollar coin"
              }

def bold(input_text):

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-."
    bold_chars = "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵-."

    output = ""

    for character in input_text:
        if character in chars:
            output += bold_chars[chars.index(character)]
        else:
            output += character 

    return output


def postPriceEdge(currencyPair, percentage, chainlinkPrice, dodoPrice, chainlinktimestamp):
    fullCurrencyPair = bold(dictionary[currencyPair])
    currencyPair = bold(currencyPair)
    percentage = bold(f"{percentage:.3f}")
    tweetText = '\n'.join([f"PRICE ADVANTAGE DETECTED FOR {currencyPair}!",
                           f"{fullCurrencyPair}",
                           f"{percentage}% better price for DODO",
                           # f"{bold('Price Difference:')} {(chainlinkPrice - dodoPrice):.3f}",
                           f"{bold('Chainlink price:')} {chainlinkPrice:.8f}",
                           f"{bold('Dodo price:')} {dodoPrice:.8f}",
                           f"Chainlink timestamp: {chainlinktimestamp}"])
    api.update_status(status=tweetText)
    return tweetText