
Paste:

```makefile
install:
	pip install -e ".[dev]"

test:
	pytest

format:
	black .

lint:
	ruff check .