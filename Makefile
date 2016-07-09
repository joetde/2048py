
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

nose:
	@nosetests -I browser -v

upgrade:
	@pip install retrying timeout-decorator selenium --upgrade
