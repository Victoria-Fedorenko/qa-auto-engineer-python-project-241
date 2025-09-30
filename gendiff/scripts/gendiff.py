import argparse
import json
from pathlib import Path


def read_files(file1, file2):

    def read_file(file_path_str):
            file_path = Path(file_path_str)
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


def format_result(equal_pairs, no_match_pairs, pairs_with_different_vals):

    big_list = equal_pairs + no_match_pairs + pairs_with_different_vals

    def sort_key(x):
        # Remove diff marker and spaces, get key name
        key_name = x.lstrip(' +-').split(':', 1)[0]
        # '-' first, '+' second, others last
        marker = 0 if x.strip().startswith('-') else 1 if x.strip().startswith('+') else 2
        return (key_name, marker)
    sorted_list = sorted(big_list, key=sort_key)
    joined = '\n'.join(sorted_list)
    result = f'{{\n{joined}\n}}'
    return result


def generate_diff(file1, file2):

    data_1, data_2 = read_files(file1, file2)
    equal_pairs = find_the_same_data(data_1, data_2)
    no_match_pairs = one_file_only(data_1, data_2)
    pairs_with_different_vals = find_different_pairs(data_1, data_2)
    result = format_result(equal_pairs, no_match_pairs, pairs_with_different_vals)

    return result
    

def main():

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    
    parser.add_argument('first_file')

    parser.add_argument('second_file')

    parser.add_argument('-f', '--format')

    args = parser.parse_args()

    result = generate_diff(args.first_file, args.second_file)

    return result


if __name__ == '__main__':
    main()