#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["requests==2.21.0"]

setup_requirements = ["requests==2.21.0"]

test_requirements = ["requests==2.21.0"]

setup(
    author="Samridha Man Shrestha",
    author_email='sms1198@nyu.edu',
    maintainer="Samridha Man Shrestha",
    maintainer_email='sms1198@nyu.edu',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: Microsoft :: Windows",
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python trading library for the Rotman Interactive Software.",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ritpytrading',
    name='ritpytrading',
    packages=find_packages(include=['ritpytrading']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/SamSamhuns/ritpytrading',
    version='0.1.5',
    zip_safe=False,
)
