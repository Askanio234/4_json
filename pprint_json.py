import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as json_file:
        return json.load(json_file)


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    filepath = input("Введите путь до файла: ")
    json_data = load_data(filepath)
    if json_data is not None:
        pretty_print_json(json_data)
    else:
        print("Некорректный путь до файла")
