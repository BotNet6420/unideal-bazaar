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
    match_list: list = key_list.copy()
    tmp_list: list = []

    for i in range(len(target)):
        for key in match_list:
            if len(key) < len(target):
                continue

            if key[i] == target[i]:
                tmp_list.append(key)
        match_list = tmp_list
        tmp_list = []

    return match_list





def weighted_cmp(key_list: list, target: str) -> str:
    top_contestant: str = ""
    top_compatibility: float = 0.0

    for key in key_list:
        match_count: int = 0
        
        for i in range(min(len(key_list), len(target))):
            if qtypo_detec():
                count += 1
        
        if (match_count/len(key)) > top_compatibility:
            top_contestant = key

    return top_contestant


def get_price(dictionary: dict, target: str) -> None:
    key_list: list = list(dictionary.keys())
    match_list: list = find_matches(key_list, target)

    match len(match_list):
        case 1:
            print(dictionary[match_list[0]])
        case 0:
            print("Item not found.\ndid you mean" + weighted_cmp(key_list, target) + "?")
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