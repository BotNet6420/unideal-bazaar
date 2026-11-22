import requests
import json

def Fetch():
    Contents = requests.get("https://api.hypixel.net/v2/skyblock/bazaar")

    with open("data.json", "w") as DataFile:
        json.dump(Contents.json(), DataFile)
    
    return


def IdSearch(Dictionary, Target):
    KeyList = Dictionary.keys()
    i = 0

    for char in Target:
        if KeyList[i] != char:
            KeyList.pop(i)
        else:
            i += 1
        
        if len(KeyList) == 1:
            return KeyList[0]

        if len(KeyList) == 0:
            return None


def FindClosestMatch(List, Target):
    ...


def PriceSearch(Dictionary, Target):
    MatchList = IdSearch(Dictionary["products"], Target)
    MatchList = IdSearch(Dictionary["products"], Target)
    
    match len(MatchList):
        case 1:
            print(Dictionary["products"][MatchList[0]]["quick_status"]["buyPrice"])
        case 0:
            print("No Item Found")
        case _:
            FindClosestMatch(MatchList, Target)
    return


def main():
    AutoFetch = False
    Fetch()

    while True:
        print("Options:     AutoFetch     Update     Item Id     Exit")
        i = input()

        match i.lower():
            case "exit":
                print("Exited")
                break
            case "autofetch":
                AutoFetch = not AutoFetch
                print("AutoFetch: " + AutoFetch)
            case "update":
                Fetch()
                print("Updated")
            case _:
                if AutoFetch == True: Fetch()

                DataFile = open("data.json", "r")
                ItemDict = json.load(DataFile)

                PriceSearch()

