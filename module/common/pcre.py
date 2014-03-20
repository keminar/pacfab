# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class pcre(base):
	def install(self):
		self.download(conf.PCRE_URL + '/' + conf.PCRE + '.tar.gz')
		self.unzip(conf.PCRE)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.PCRE):
			run('./configure -prefix=/usr/local/pcre && make && make install')
	def check(self):
		with quiet():
			output = run('test /usr/local/pcre ;echo $?')
			return output
