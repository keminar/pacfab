# encoding: utf-8

import conf
from fabric.api import *
from module.common.base import base
class cmake(base):
	def install(self):
		self.download(conf.CMAKE_URL + '/' + conf.CMAKE + '.tar.gz')
		self.unzip(conf.CMAKE)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.CMAKE):
			run('./bootstrap && make && make install')
	def check(self):
		with quiet():
			output = run('which cmake >/dev/null 2>&1;echo $?')
			return output
