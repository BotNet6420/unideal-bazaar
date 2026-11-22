import requests
import json

def fetch():
    contents = requests.get("https://api.hypixel.net/v2/skyblock/bazaar")

    with open("data.json", "w") as DataFile:
        json.dump(contents.json(), DataFile)
    
    return


def id_search(dictionary, target):
    key_list = dictionary.keys()
    i = 0

    for char in target:
        if key_list[i] != char:
            key_list.pop(i)
        else:
            i += 1
        
        if len(key_list) == 1:
            return key_list[0]

        if len(key_list) == 0:
            return None


def find_closest_match(list, target):
    ...


def price_search(dictionary, target):
    match_list = id_search(dictionary["products"], target)
    match_list = id_search(dictionary["products"], target)
    
    match len(match_list):
        case 1:
            print(dictionary["products"][match_list[0]]["quick_status"]["buyPrice"])
        case 0:
            print("No Item Found")
        case _:
            find_closest_match(match_list, target)
    return


def main():
    auto_fetch = False
    fetch()

    while True:
        print("Options:     AutoFetch     Update     Item Id     Exit")
        i = input()

        match i.lower():
            case "exit":
                print("Exited")
                break
            case "autofetch":
                auto_fetch = not auto_fetch
                print("AutoFetch: " + auto_fetch)
            case "update":
                fetch()
                print("Updated")
            case _:
                if auto_fetch == True: fetch()

                data_file = open("data.json", "r")
                item_dict = json.load(data_file)

                price_search()

