#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='resilient_lib',
    version='1.0.0',
    url='https://ibm.biz/resilient',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="library for resilient-circuits functions",
    long_description="This package contains common library calls which facilitate the development of functions for IBM Resilient.",
    install_requires=[
        'bs4',
        'resilient_circuits>=30.0.0',
        'six'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    tests_require=['pytest'],
    entry_points={
        "resilient.circuits.configsection": ["gen_config = resilient_lib.util.config:config_section_data"]
    }
)