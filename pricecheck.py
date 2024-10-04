# !pricecheck takes in one or more items and performs a price check on them using the Janice API

# Usage:
# !pricecheck [market (optional)] [item] [qty (optional)] [item (optional)] [qty (optional)] ... 
# [market] is an optional value specifying a market to use
# [item] is an item to check, it must be placed in quotes if it is longer than one word
# [qty] is a quantity to apply to the preceding item, it is optional even when checking multiple items

import requests

def check(args):
    return