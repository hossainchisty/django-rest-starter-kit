.PHONY: install migrate superuser run test lint format clean build up down

install:
	pip install -r requirements/development.txt
	pre-commit install

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

superuser:
	python manage.py createsuperuser

run:
	python manage.py runserver

test:
	pytest

test-cov:
	pytest --cov=apps --cov-report=html

lint:
	flake8
	pylint apps/
	mypy apps/

format:
	black .
	isort .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down
