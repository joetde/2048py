
all: clean test install

clean:
	@rm -rf *.egg*
	@rm -rf build
	@rm -rf dist

test: lint nose

lint:
	@pylint src/*

install:
	@pip install .

test_install:
	@2048.py --help

uninstall:
	@pip uninstall -y 2048py

nose:
	@nosetests --with-coverage --cover-package=lib2048 tests/test_*.py

upgrade:
	@pip install retrying timeout-decorator selenium --upgrade
