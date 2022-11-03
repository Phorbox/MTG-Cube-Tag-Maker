import requests
import json
import re


def writeJson(name, dict):
    jsonFile = open(name, "w")
    jsonFile.write(json.dumps(dict, indent=4))
    jsonFile.close()

def addJsonToDict(src,dest,fields):
    for each in src["data"]:
        dicter = {}
        for eachers in fields:
            tempStr = f"{each[eachers]}"
            tempStr = tempStr.replace("—", "-")
            tempStr = tempStr.replace("\u2605", "")
            tempStr = tempStr.replace("•", "*")
            dicter[eachers] = tempStr
        dest[each["name"]] = dicter

def urlToDict(url):
    return (requests.get(url).json())

def betterOracleText():
    cleanFlavor()
    pass

def cleanFlavor():
    pass

api_url = "https://api.scryfall.com/cards/search?q=set%3A40k+is%3Afoil&unique=cards&as=grid&order=set"
full = urlToDict(api_url)

felds = ["cmc", "type_line", "colors", "set_name",
          "collector_number", "rarity", "color_identity", "oracle_text"]

bigDict = {}
hasMore = full["has_more"]
addJsonToDict(full,bigDict,felds)

while (hasMore):
    full = urlToDict(full["next_page"])
    addJsonToDict(full,bigDict,felds)
    hasMore = full["has_more"]

for each in bigDict:
    print(bigDict[each]["collector_number"])





writeJson("big.json", bigDict)
