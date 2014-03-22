# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class pcre(base):
	def install(self):
		self.download(conf.PCRE_URL + '/' + conf.PCRE + '.tar.gz')
		self.unzip(conf.PCRE)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.PCRE):
			run('./configure -prefix=/usr/local/pcre')
			run('make && make install')
		run('touch /usr/local/pcre/.install.log')

	def check(self):
		return self.test('/usr/local/pcre/.install.log')
