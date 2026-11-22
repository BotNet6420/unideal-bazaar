import requests
import json

from requests import Response


def fetch() -> dict:
    contents: Response = requests.get("https://api.hypixel.net/v2/skyblock/bazaar")
    raw_dictionary: dict = contents.json()["products"]

    temporary_list = list()
    for item in raw_dictionary.values():
        temporary_list.append(item["quick_status"]["buyPrice"])

    return dict(zip(raw_dictionary.keys(), temporary_list))


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

def price_search(dictionary: dict, target: str) -> None:
    match_list = id_search(dictionary, target)
    
    match len(match_list):
        case 1:
            print(dictionary["products"][match_list[0]]["quick_status"]["buyPrice"])
        case 0:
            print("No Item Found")
        case _:
            find_closest_match(match_list, target)
    return None


def main() -> None:
    auto_fetch: bool = False
    item_dict = fetch()

    while True:
        print("Options:     AutoFetch     Update     Item Id     Exit")
        input_string: str = input()

        match input_string.lower():
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


                price_search(item_dict, input_string)
    return

if __name__ == "__main__":
    main()