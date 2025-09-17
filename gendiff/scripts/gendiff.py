import argparse
import json
from path import Path

FILE1 = Path('..', '..', 'file1.json')
FILE2 = Path('..', '..', 'file2.json')

def read_files(file1=FILE1, file2=FILE1):

    config_file_1 = json.load(file1)
    config_file_2 = json.load(file2)

    return config_flie_1, config_file_2



def main():

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    
    parser.add_argument('first_file')

    parser.add_argument('second_file')

    parser.add_argument('-f', '--format')

    parser.parse_args()

    config_file_1, config_file_2 = read_files()

if __name__ == '__main__':
    main()