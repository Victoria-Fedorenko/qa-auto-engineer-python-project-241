
import argparse

from gendiff.scripts.parse_data import get_categorized_data, read_files
from gendiff.scripts.stylish import stylish
from gendiff.scripts.plain import plain


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