# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class mhash(base):
	def install(self):
		self.download(conf.MHASH_URL + '/' + conf.MHASH + '.tar.gz')
		self.unzip(conf.MHASH)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.MHASH):
			run('./configure --prefix=' + conf.INSTALL_DIR + '/opt/mhash')
			run('make && make install')
		run('touch ' + conf.INSTALL_DIR + '/opt/mhash/.install.log')

	def check(self):
		return self.test(conf.INSTALL_DIR + '/opt/mhash/.install.log')
