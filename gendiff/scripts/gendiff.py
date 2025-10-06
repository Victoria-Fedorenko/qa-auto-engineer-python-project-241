
import argparse

from gendiff.scripts.parse_data import get_categorized_data, read_files


def format_the_same_data(same_data):
    result = []
    for k, val in same_data.items():
        result.append(f'    {k}: {val}')
    return result


def format_removed_data(removed_data):
    result = []
    for k, val in removed_data.items():
        result.append(f'  - {k}: {val}'.lower())
    return result


def format_added_data(added_data):
    result = []
    for k, val in added_data.items():
        result.append(f'  + {k}: {val}'.lower())
    return result


def format_changed_data(before_change, after_change):
    result = []
    for k in before_change.keys():
        val1 = before_change[k]
        val2 = after_change[k]
        result.append(f'  - {k}: {val1}')
        result.append(f'  + {k}: {val2}')
    return result


def stylish(same_data, removed_data, added_data, before_change, after_change):

    same_data_formatted = format_the_same_data(same_data)
    removed_data_formatted = format_removed_data(removed_data)
    added_data_formatted = format_added_data(added_data)
    changed_data_formatted = format_changed_data(before_change, after_change)

    big_list = (same_data_formatted +
                removed_data_formatted +
                added_data_formatted + 
                changed_data_formatted)

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
    (
        same_data,
        removed_data,
        added_data,
        before_change,
        after_change,
    ) = get_categorized_data(
        data_1,
        data_2,
    )
    
    result = formatter(
        same_data,
        removed_data,
        added_data,
        before_change,
        after_change,
    )

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