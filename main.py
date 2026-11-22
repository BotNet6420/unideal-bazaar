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


def find_matches(key_list: list, target: str) -> list:

    input_list: list = key_list.copy()
    match_list: list = []

    for i in range(len(target)):
        for key in input_list:
            if len(key) < len(target):
                continue

            if key[i] == target[i]:
                match_list.append(key)
        input_list = match_list
        match_list = []

    return input_list


def weighted_strcmp(key_list: list, target: str) -> str:
    ...

def get_price(dictionary: dict, target: str) -> None:
    key_list: list = list(dictionary.keys())
    match_list: list = find_matches(key_list, target)

    match len(match_list):
        case 1:
            print(dictionary[match_list[0]])
        case 0:
            print("Item not found did you mean" + weighted_strcmp(key_list, target) + "?")
        case _:
            print(match_list)
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