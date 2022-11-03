import json,re

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

def openJson(name):
    jsonFile = open(name)
    returner = json.load(jsonFile)
    jsonFile.close()
    return returner

def typeLineToTags(typeLine):
    return re.split(r" -* *",typeLine)

def addEvasion(textToSearch,tags):
    textList = ["(can't be blocked)","flying","trample","menace","haste"]
    evasionRegex = r""
    for each in textList:
        evasionRegex += (each + "|")
    evasionRegex = evasionRegex[:-1]
    if(re.search(evasionRegex,textToSearch)):
        tags += ["Evasion"]



bigDict = openJson("big.json")
for each in bigDict:
    currentNode = bigDict[each]
    tags = []
    tags += typeLineToTags(currentNode["type_line"])
    addEvasion(currentNode["oracle_text"],tags)
    currentNode["tags"] = tags
    bigDict[each] = currentNode
    
writeJson("40kCube.json", bigDict)

