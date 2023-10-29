.PHONY: init test lint format build mypy

CODE = {{cookiecutter.package_name}}
PYVENVCFG = .venv/pyvenv.cfg

$(PYVENVCFG):
	$(MAKE) init

init:
	poetry install

test: $(PYVENVCFG)
	poetry run pytest

lint: $(PYVENVCFG)
	poetry run black --check --diff $(CODE)
	poetry run ruff check $(CODE)

format: $(PYVENVCFG)
	poetry run black $(CODE)

build: $(PYVENVCFG)
	poetry build

mypy: $(PYVENVCFG)
	poetry run mypy $(CODE)
