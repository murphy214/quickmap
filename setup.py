#!/usr/bin/env python

from setuptools import setup, find_packages
import os
setup(name='quickmap',
      version='1.0',
      description='A Python library for map integration.',
      author='Bennett Murphy',
      author_email='murphy214@live.marshall.edu',
      url='https://github.com/murphy214',
      #dependency_links=['http://github.com/murphy214/nlgeojson/tarball/master#egg=package-1.0'],#http://github.com/murphy214/pipeleaflet/tarball/master#egg=package-1.1','http://github.com/murphy214/pipevts/tarball/master#egg=package-1.0','http://github.com/murphy214/pipegls/tarball/master#egg=package-1.0']
      scripts = ['bin/map'],
      #dependency_links=['http://github.com/murphy214/nlgeojson.git#egg=nlgeojson-1.0']#http://github.com/murphy214/pipeleaflet/tarball/master#egg=package-1.1','http://github.com/murphy214/pipevts/tarball/master#egg=package-1.0','http://github.com/murphy214/pipegls/tarball/master#egg=package-1.0']

      )
