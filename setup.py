#!/usr/bin/env python

from setuptools import setup

setup(
    setup_requires=['pbr'],
    install_requires=['requests>=1.1'],
    pbr=True,
    version="0.4.0",
)
