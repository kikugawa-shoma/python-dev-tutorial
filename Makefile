SHELL=/bin/bash

.PHONY: unittest doctest

unittest1:
	python3 -m unittest discover -v

unittest2:
	python3 -m unittest fizzbuzz.tests.test_fizzbuzz -v

doctest:
	python3 -m doctest -v fizzbuzz/*.py

