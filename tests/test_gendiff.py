from gendiff.scripts.gendiff import generate_diff

good_result_1 = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

def test_generate_diff(): 
    assert generate_diff('test_data/file1.json', 'test_data/file2.json') == good_result_1
    assert generate_diff('test_data/filepath1.yml', 'test_data/filepath2.yml') == good_result_1