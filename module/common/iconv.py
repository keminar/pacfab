# encoding: utf-8

import conf
from fabric.api import *
from module.common.base import base
class iconv(base):
	def install(self):
		self.download(conf.GNU_URL + '/libiconv/' + conf.ICONV + '.tar.gz')
		self.unzip(conf.ICONV)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.ICONV):
			run('./configure --prefix=' + conf.INSTALL_DIR + '/opt/libiconv --enable-extra-encodings')
			run('make && make install')

	def check(self):
		with quiet():
			output = run('test -e ' + conf.INSTALL_DIR + '/opt/libiconv ;echo $?')
			return output
