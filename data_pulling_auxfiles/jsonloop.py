import requests
import json
import os

#function to write to files json data pulled from eBay API

save_path = '/Users/jzymet/itemSpecifics3/'
with open("getItemrequest.txt") as i:
    r = i.read()
    with open('item.json') as j:
        x = json.load(j)
        for item in x["findCompletedItemsResponse"][0]["searchResult"][0]["item"]:
            itemId = item["itemId"][0]
            url = r % itemId
            data = requests.get(url)
            with open(os.path.join(save_path, f'{itemId}.json'), 'w', encoding='utf8') as f:
                json.dump(json.JSONDecoder().decode(data.text), f)