
all: clean lint install

clean:
	@rm -rf *.egg*
	@rm -rf build
	@rm -rf dist

lint:
	@pylint src/*

install:
	@python setup.py install
