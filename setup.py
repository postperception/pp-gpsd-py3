#!/usr/bin/env python3

from setuptools import setup

setup(
        name='pp-gpsd-py3',
        version='1.0.0',
        packages=['gpsd'],
        url='https://github.com/postperception/pp-gpsd-py3',
        license='MIT',
        author='Sam Liu',
        author_email='sam@postperception.com',
        description='Python 3 library for working with gpsd. Forked from gpsd-py3.',
        keywords=["gps", "gpsd"],
        classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Development Status :: 5 - Stable",
            "Operating System :: POSIX :: Linux",
            "License :: OSI Approved :: MIT License"
        ],
)
