import json

from pathlib import Path

import yaml


def read_files(file1, file2):

    def read_file(file_path_str):
        file_path = Path(file_path_str)
        file_extension = file_path.suffix
        if file_extension in ['.yml', '.yaml']:
            with open(file_path, 'r') as my_file:
                try:
                    my_data = yaml.safe_load(my_file)
                    return my_data
                except yaml.YAMLError as e:
                    print(f"Ошибка в YAML: {e}")
                    print("Содержимое файла:")
                    print(my_file.read())
        elif file_extension == '.json':
            with open(file_path, 'r') as my_file:
                try:
                    my_data = json.load(my_file)
                    return my_data
                except json.JSONDecodeError as e:
                    print(f"Ошибка в JSON: {e}")
                    print("Содержимое файла:")
                    print(my_file.read())    

    data_1 = read_file(file1)
    data_2 = read_file(file2)

    return data_1, data_2


def find_the_same_data(data_1, data_2):

    keys_1 = data_1.keys()
    keys_2 = data_2.keys()

    result = []

    for k in keys_1:

        if k in keys_2:

            if data_1[k] == data_2[k]:

                val = data_1[k]

                str_to_append = f'    {k}: {val}'
                result.append(str_to_append)
    
    return result


def one_file_only(data_1, data_2):

    keys_1 = data_1.keys()
    keys_2 = data_2.keys()

    result = []

    for k in keys_1:

        if k not in keys_2:

            val = data_1[k]

            str_to_append = f'  - {k}: {val}'
            result.append(str_to_append.lower())

    for k in keys_2:

        if k not in keys_1:

            val = data_2[k]

            str_to_append = f'  + {k}: {val}'
            result.append(str_to_append.lower())
    
    return result


def find_different_pairs(data_1, data_2):

    keys_1 = data_1.keys()
    keys_2 = data_2.keys()

    result = []

    for k in keys_1:

        if k in keys_2:

            if data_1[k] != data_2[k]:

                val1 = data_1[k]
                val2 = data_2[k]

                str_to_append_1 = f'  - {k}: {val1}'
                str_to_append_2 = f'  + {k}: {val2}'

                result.append(str_to_append_1)
                result.append(str_to_append_2)

    return result


def get_big_list(data_1, data_2):

    equal_pairs = find_the_same_data(data_1, data_2)
    no_match_pairs = one_file_only(data_1, data_2)
    pairs_with_different_vals = find_different_pairs(data_1, data_2)

    big_list = equal_pairs + no_match_pairs + pairs_with_different_vals

    return big_list