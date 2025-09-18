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

    
    



def main():

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    
    parser.add_argument('first_file')

    parser.add_argument('second_file')

    parser.add_argument('-f', '--format')

    args = parser.parse_args()

    data_1, data_2 = read_files(args.first_file, args.second_file)

    #return data_1, data_2

    

if __name__ == '__main__':
    main()