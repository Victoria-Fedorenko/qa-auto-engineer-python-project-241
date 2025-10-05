import argparse

from gendiff.scripts.parse_data import get_big_list, read_files


def stylish(big_list):

    def sort_key(x):
        key_name = x.lstrip(' +-').split(':', 1)[0]
        stripped = x.strip()
        if stripped.startswith('-'):
            marker = 0
        elif stripped.startswith('+'):
            marker = 1
        else:
            marker = 2
        return (key_name, marker)
    sorted_list = sorted(big_list, key=sort_key)
    joined = '\n'.join(sorted_list)
    result = f'{{\n{joined}\n}}'
    return result


def generate_diff(file1, file2, formatter=stylish):

    data_1, data_2 = read_files(file1, file2)
    big_list = get_big_list(data_1, data_2)
    result = formatter(big_list)

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