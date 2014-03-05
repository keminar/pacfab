#!/usr/bin/python
# encoding: utf-8

import os
import sys
import conf
from fabric.api import *
def install_cmake():
	with cd(conf.BASE_DIR + '/dist'):
		run('wget -c ' + conf.CMAKE_URL + conf.CMAKE + '.tar.gz')
	with cd(conf.BASE_DIR + '/src'):
		run('tar zxf ../dist/' + conf.CMAKE + '.tar.gz')
	with cd(conf.BASE_DIR + '/src/' + conf.CMAKE):
		run('./bootstrap && make && make install')
