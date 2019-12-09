#!/usr/bin/env python

# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

from setuptools import find_packages, setup

tests_require = [
    'coverage',
    'pytest',
]

setup(
    name='template',
    version='0.0.1',
    description='tbd',
    long_description='tbd',
    license='tbd',
    url='https://tbd.org',
    author='Carsten Rösnick-Neugebauer',
    author_email='croesnick@gmail.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=[],
    extras_require={
        'test': tests_require,
        'dev': tests_require,
    },
    zip_safe=False,
)
