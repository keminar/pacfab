# encoding: utf-8

import re
import conf
from fabric.api import *
from core.base import base
class redis(base):
	def install(self):
		self.download(conf.REDIS_URL + '/' + conf.REDIS + '.tar.gz')
		self.unzip(conf.REDIS)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.REDIS):
			run('make && make PREFIX=' + conf.INSTALL_DIR + '/opt/redis install')
		self.service('redis')
		self.path('redis')
		run('touch ' + conf.INSTALL_DIR + '/opt/redis/.install.log')
		self.instance()

	def instance(self, port = '6379'):
		dstPath = conf.INSTALL_DIR + '/srv/redis/' + port
		run('mkdir -p ' + dstPath + '/data')
		put(conf.BASE_DIR + '/conf/redis/redis.conf', dstPath)
		run('sed -i "s/<port>/' + port + '/g" ' + dstPath + '/redis.conf')
		run('sed -i "s/<INSTALL_DIR>/' + re.escape(conf.INSTALL_DIR) + '/g" ' + dstPath + '/redis.conf')
		run(conf.INSTALL_DIR + '/bin/redis.init start ' + port)

	def check(self):
		return self.test(conf.INSTALL_DIR + '/opt/redis/.install.log')
