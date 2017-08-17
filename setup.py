# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='py_csv_to_json',
    version='0.0.1',
    description='python code to covert csv file to json',
    long_description=readme,
    author='Quadyster Cloud Devs',
    author_email='',
    url='https://github.com/quad-cloud/py_csv_to_json_02.git',
    packages=find_packages(exclude=('tests', 'docs'))
)
