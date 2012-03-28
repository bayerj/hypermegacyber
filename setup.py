#! /usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Justin Bayer, bayer.justin@googlemail.com'


from setuptools import setup, find_packages


setup(
    name="hypermegacyber",
    version="pre-0.1",
    description="basic hybrid monte carlo",
    license="BSD",
    keywords="statistics markov-chain monte carlo sampling hybrid",
    packages=find_packages(exclude=['examples', 'docs']),
    include_package_data=True,
)

