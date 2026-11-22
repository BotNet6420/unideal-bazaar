import requests
import json

from requests import Response


def fetch() -> None:
    contents: Response = requests.get("https://api.hypixel.net/v2/skyblock/bazaar")

    with open("data.json", "w") as DataFile:
        json.dump(contents.json(), DataFile)
    
    return


# TODO: define return type
def id_search(dictionary: dict, target: str):
    # TODO:
    #   The blow type is "dict_keys" which is a "view" of the original dictionary
    #   Does not behave like a normal list:
    #   - Deos not define bracket indexing via "[]"
    #   - Does not define a "pop" method
    #   - Modifying this could result in the modification of the original dictionary
    #   1. Wrap the left side in "list(...)" constructor
    #   2. Define variable type
    key_list: list = list(dictionary.keys())
    i = 0

    # TODO: Missing return on some paths (e.g. exiting loop)
    for char in target:
        if key_list[i] != char:
            key_list.pop(i)
        else:
            i += 1
    return key_list


# TODO: parameter name "list" shadows built-in type
#   types not specified
#   define return type
def find_closest_match(list, target):
    ...

# TODO: define return type
def price_search(dictionary: dict, target: str):
    match_list = id_search(dictionary["products"], target)
    
    match len(match_list):
        case 1:
            print(dictionary["products"][match_list[0]]["quick_status"]["buyPrice"])
        case 0:
            print("No Item Found")
        case _:
            find_closest_match(match_list, target)
    return


def main() -> None:
    auto_fetch: bool = False
    fetch()

    while True:
        print("Options:     AutoFetch     Update     Item Id     Exit")
        i: str = input()

        match i.lower():
            case "exit":
                print("Exited")
                break
            case "autofetch":
                auto_fetch = not auto_fetch
                print("AutoFetch: " + str(auto_fetch))
            case "update":
                fetch()
                print("Updated")
            case _:
                if auto_fetch: fetch()

                data_file = open("data.json", "r")
                item_dict = json.load(data_file)

                # TODO: function call missing parameters
                price_search()
    return

if __name__ == "__main__":
    main()