#!/usr/bin/env python

# http://www.scotttorborg.com/python-packaging/
# http://guide.python-distribute.org/creation.html

from setuptools import setup

setup(
	# package metadata
	name = "biofabric",
	version = "0.1.0",
	description = "Python implementation of the BioFabric network visualization technique",
	long_description = open("README.rst").read(),
	url = "https://github.com/ajmazurie/biofabric",
	license = open("LICENSE.txt").read(),
	classifiers = (
		"Development Status :: 3 - Alpha",
		"Environment :: Console",
		"Intended Audience :: Science/Research",
		"Operating System :: OS Independent",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Topic :: Scientific/Engineering :: Visualization",
	),
	install_requires = ("networkx",	"pyx"),

	# author metadata
	author = "Aurelien Mazurie",
	author_email = "ajmazurie@oenone.net",

	# package manifest
	packages = ["biofabric"],
	package_dir = {'': "lib"},
)