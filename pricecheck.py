# !pricecheck takes in one or more items and performs a price check on them using the Janice API

# Usage:
# !pricecheck [market (optional)] [item] [qty (optional)] [item (optional)] [qty (optional)] ... 
# [market] is an optional value specifying a market to use
# [item] is an item to check, it must be placed in quotes if it is longer than one word
# [qty] is a quantity to apply to the preceding item, it is optional even when checking multiple items

import requests
import os
import json

from dotenv import load_dotenv

load_dotenv()
JANICE_TOKEN = os.getenv("JANICE_TOKEN")

market_ids = {
    
}

def check(args):
    # Craft the response
    response = ""

    market_index = market_ids["Jita"]
    janice_query = ""

    # If a valid market is passed as the first argument, use that to set the market
    if args[0] in market_ids:
        market_index = market_ids[args[0]]
        
        for item in args[1:]:
            # Prepend item with a newline if it's not an item, to handle given quantities          
            if item.isnumeric():
                janice_query += ""
            else:
                janice_query += "\n"

            janice_query += item
    else:
        for item in args[0:]:
            # Prepend item with a newline if it's not an item, to handle given quantities          
            if item.isnumeric():
                janice_query += ""
            else:
                janice_query += "\n"

            janice_query += item
    
    appraisal_value = "{:,}".format(round(appraise(market_index, janice_query), 2))

    return f"{appraisal_value} ISK"

def appraise(market, query):
    headers = {
        'accept': 'application/json',
        'X-ApiKey': JANICE_TOKEN,
        'Content-Type': 'text/plain',
    }

    params = {
        'market': market,
        'designation': 'wtb',
        'pricing': 'sell',
        'pricingVariant': 'top5percent',
        'persist': 'false',
        'compactize': 'true',
        'pricePercentage': '1',
    }

    data = query

    response = json.loads(requests.post('https://janice.e-351.com/api/rest/v2/appraisal', params=params, headers=headers, data=data).text)

    return response.get("effectivePrices").get("totalSellPrice")

# Get markets from Janice and populate the dictionary
def get_markets():
    print("Updating Janice market info")

    headers = {
        'accept': 'application/json',
        'X-ApiKey': JANICE_TOKEN
    }

    response = json.loads(requests.get('https://janice.e-351.com/api/rest/v2/markets', headers=headers).text)

    for item in response:
        name = item["name"]
        id = item["id"]

        if name == "Jita 4-4":
            name = "Jita"

        market_ids[name] = id

get_markets()