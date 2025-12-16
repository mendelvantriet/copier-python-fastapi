.PHONY: install
install:
	pip install --require-virtualenv --upgrade pip
	pip install --require-virtualenv -r requirements.txt

.PHONY: dirty
dirty:
	copier copy -r HEAD . $(destination)$(dest)$(d)

.PHONY: test
test:
	ctt
