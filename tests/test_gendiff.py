from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.stylish import stylish
from gendiff.scripts.plain import plain
import json
from gendiff.scripts.json import json_formatter


def load_expected(name):

    path = f'tests/expected/{name}'
    with open(path, 'r') as fh:
        return fh.read()


def test_generate_diff():
    expected_stylish = load_expected('stylish.txt')
    expected_plain = load_expected('plain.txt')
    expected_json = json.loads(load_expected('json.json')), indent=2

    assert generate_diff('tests/test_data/file1.json', 
                         'tests/test_data/file2.json') == expected_stylish
    assert generate_diff('tests/test_data/file1.json', 
                         'tests/test_data/file2.json', 
                         stylish) == expected_stylish
    assert generate_diff('tests/test_data/filepath1.yml', 
                         'tests/test_data/filepath2.yml') == expected_stylish
    assert generate_diff('tests/test_data/file1.json', 
                         'tests/test_data/file2.json', 
                         plain) == expected_plain
    assert json.loads(generate_diff(
                        'tests/test_data/file1.json', 
                         'tests/test_data/file2.json', 
                         json_formatter)) == expected_json
    