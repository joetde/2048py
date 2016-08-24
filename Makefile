
all: clean test install

clean:
	@rm -rf *.egg*
	@rm -rf build
	@rm -rf dist

test: lint nose

lint:
	@pylint src/*

install:
	@pip install -U .

run:
	@2048bot.py

test_install:
	@2048bot.py --help

uninstall:
	@pip uninstall -y 2048py

nose:
	@nosetests --with-coverage --cover-package=lib2048 tst/test_*.py

upgrade:
	@pip install retrying timeout-decorator selenium --upgrade

kill_node:
	@kill -9 $(shell ps aux | grep node | awk '{print $$1}')