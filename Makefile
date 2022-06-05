install:
	poetry install

brain-games:
	poetry run brain-games

build: lint
	poetry build

publish: build
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 brain_games