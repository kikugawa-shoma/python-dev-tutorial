SHELL=/usr/bin/bash

.PHONY: unittest doctest

unittest:
	python -m unittest fizzbuzz.tests.test_fizzbuzz -v

doctest:
	python -m doctest -v fizzbuzz/*.py
