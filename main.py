import requests
import json

from requests import Response


def fetch() -> dict:
    contents: Response = requests.get("https://api.hypixel.net/v2/skyblock/bazaar")
    raw_dictionary: dict = contents.json()["products"]

    id_price_dict: dict = {}
    for item in raw_dictionary.keys():
        id_price_dict[item] = raw_dictionary[item]["quick_status"]["buyPrice"]

    return id_price_dict


def id_search(match_list: list, target: str) -> list:

    i = 0

    # TODO: Missing return on some paths (e.g. exiting loop)
    for char in target:
        if match_list[i] != char:
            match_list.pop(i)
        else:
            i += 1
    return match_list


# TODO: parameter name "list" shadows built-in type
#   types not specified
#   define return type
def find_closest_match(list, target):
    ...

def get_price(dictionary: dict, target: str) -> None:
    match_list: list = id_search(list(dictionary.keys()), target)

    match len(match_list):
        case 1:
            print(dictionary[target])
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

                get_price(item_dict, input_string)
    return

if __name__ == "__main__":
    main()