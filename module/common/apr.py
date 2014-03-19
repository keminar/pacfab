# encoding: utf-8

import conf
from fabric.api import *
from module.common.base import base
class apr(base):
	def install(self):
		self.download(conf.APACHE_URL + '/apr/' + conf.APR + '.tar.gz')
		self.unzip(conf.APR)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.APR):
			run('./configure --prefix=/usr/local/apr')
			run('make && make install')
		self.download(conf.APACHE_URL + '/apr/' + conf.APR_UTIL + '.tar.gz')
		self.unzip(conf.APR_UTIL)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.APR_UTIL):
			run('./configure --prefix=/usr/local/apr-util --with-apr=/usr/local/apr')
			run('make && make install')

	def check(self):
		with quiet():
			output = run('test -e /usr/local/apr-util >/dev/null 2>&1; echo $?')
			return output
