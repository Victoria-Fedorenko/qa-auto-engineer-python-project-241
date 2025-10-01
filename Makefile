build:
	uv build

lint:
	uv run ruff check gendiff

tests:
	uv run pytest