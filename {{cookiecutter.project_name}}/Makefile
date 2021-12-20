.PHONY: init test lint format build

CODE = {{cookiecutter.package_name}}

poetry.lock:
	$(MAKE) init

init:
	poetry install

test: poetry.lock
	poetry run pytest

lint: poetry.lock
	poetry run black --check --diff $(CODE)
	poetry run flake8 {{cookiecutter.package_name}} --count --show-source --statistics

format: poetry.lock
	poetry run black $(CODE)

build: poetry.lock
	poetry build
