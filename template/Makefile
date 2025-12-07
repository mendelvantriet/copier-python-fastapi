.PHONY: install
install:
	pip install --require-virtualenv --upgrade pip
	pip install --require-virtualenv ".[dev]"

.PHONY: lock
lock:
	pip-compile -o requirements.txt pyproject.toml

.PHONY: update
update:
	copier update --vcs-ref=$(tag) .
