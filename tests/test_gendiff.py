from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.stylish import stylish
from gendiff.scripts.plain import plain

good_result_stylish = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

good_result_plain = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

def test_generate_diff():
  assert generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.json') == good_result_stylish
  assert generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.json', stylish) == good_result_stylish
  assert generate_diff('tests/test_data/filepath1.yml', 'tests/test_data/filepath2.yml') == good_result_stylish
  assert generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.json', plain) == good_result_plain 