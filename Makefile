SHELL=/bin/bash

.PHONY: unittest doctest

unittest1:
	python -m unittest discover -v

unittest2:
	python -m unittest fizzbuzz.tests.test_fizzbuzz -v

doctest:
	python -m doctest -v fizzbuzz/*.py

install:
	python setup.py install

uninstall:
	pip3 uninstall fizzbuzz -y

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	find . -name "*pycache*" | xargs rm -rf


