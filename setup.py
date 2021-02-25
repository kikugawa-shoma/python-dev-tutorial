from setuptools import setup, find_packages, version

setup(
    name='fizzbuzz',
    version="0.0.1",
    description='Fizz Buzz program',
    author='kikugawa',
    url='https://github.com/sotetsuk/python-dev-tutorial/issues/13',
    author_email='kikugawa.s.shukatsu@gmail.com',
    license='MIT',
    install_requires=[],
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "programming Language :: Python  :: 3.8",
        "License :: OSI Approved :: MIT License"
    ]
)
