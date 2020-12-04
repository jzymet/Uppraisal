import csv
import json

#functions to help organize json data pulled from eBay API into csv

def get_bid_count(b):
    if 'sellingStatus' in b and len(b["sellingStatus"]):
        stat = b["sellingStatus"][0]
        if 'bidCount' in stat and len(stat["bidCount"]):
            return stat["bidCount"][0]
    return 'null'

def get_watch_count(b):
    if 'listingInfo' in b and len(b["listingInfo"]):
        stat = b["listingInfo"][0]
        if 'watchCount' in stat and len(stat["watchCount"]):
            return stat["watchCount"][0]
    return 'null'

with open('item.json') as f:
    j = json.load(f)
    f = csv.writer(open("test99.csv", "w"))
    f.writerow(["itemId", "title", "categoryId", "categoryName", "viewItemURL", "conditionDisplayName", "currentPrice", "bidCount", "sellingState", "watchCount"])
    for x in j["findCompletedItemsResponse"][0]["searchResult"][0]["item"]:
        f.writerow([x["itemId"][0],
                    x["title"][0],
                    x["primaryCategory"][0]["categoryId"][0],
                    x["primaryCategory"][0]["categoryName"][0],
                    x["viewItemURL"][0],
                    x["condition"][0]["conditionDisplayName"][0],
                    x["sellingStatus"][0]["currentPrice"][0],
                    get_bid_count(x),
                    x["sellingStatus"][0]["sellingState"][0],
                    get_watch_count(x)])