This CLI tool can help you to compare two configuration files using gendiff function.
You can compare json-files and yml-files.

To install the package clone the repository and enter the project folder.
After that you can build the project with
```bash
uv build
```

You can use this tool with or without format option. 
Format options available: stylish, plain, json. Watch demonstration to see the difference. 

EXAMPLE:

```bash
gendiff file1.json file2.json
# or with format option
gendiff -f json file1.yml file2.yml
```

[Watch demonstration of usage with or without formatters](https://asciinema.org/a/QkJVHlLIs8CfYyvCqWVTwhQXy)

[Watch demonstration for json files](https://asciinema.org/a/YONoWweyjVdWYWzxh994hgtza) 

[Watch demonstration for yaml files](https://asciinema.org/a/4eqZF5sM4VduEwwfLEmvYTCsq)

[Watch demonstration of json-formatter](https://asciinema.org/a/2AGCrM6ckuPikuX4a7w8rm9XA)


### Hexlet tests and linter status:
[![Actions Status](https://github.com/Victoria-Fedorenko/qa-auto-engineer-python-project-241/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Victoria-Fedorenko/qa-auto-engineer-python-project-241/actions)
[![Lint, Test, and SonarQube Analysis](https://github.com/Victoria-Fedorenko/qa-auto-engineer-python-project-241/actions/workflows/test_lint_sonar.yml/badge.svg)](https://github.com/Victoria-Fedorenko/qa-auto-engineer-python-project-241/actions/workflows/test_lint_sonar.yml)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Victoria-Fedorenko_qa-auto-engineer-python-project-241&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Victoria-Fedorenko_qa-auto-engineer-python-project-241)
