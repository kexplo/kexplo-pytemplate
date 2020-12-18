.PHONY: init test lint format build

CODE = {{cookiecutter.package_name}}

init:
	poetry install

test:
	poetry run pytest

lint:
	poetry run black --line-length=79 --check --diff $(CODE)

format:
	poetry run black --line-length=79 $(CODE)

build:
	poetry build
