# encoding: utf-8

import conf
from fabric.api import *

class init(object):
	def __init__(self):
		run('mkdir -p ' + conf.INSTALL_DIR + '/{bin,opt,srv}')
		run('mkdir -p ' + conf.BASE_DIR + '/dist/src')
