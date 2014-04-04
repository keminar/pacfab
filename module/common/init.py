# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
class init(base):
	def prepare(self):
		run('mkdir -p ' + conf.INSTALL_DIR + '/{app,bin,lib,opt,srv,var}')
		run('mkdir -p ' + conf.BASE_DIR + '/dist/src')
		if (self.test(conf.INSTALL_DIR + '/bin/profile.sh') == "1"):
			run('echo "#!/bin/bash" > ' + conf.INSTALL_DIR + '/bin/profile.sh')
			run('echo "export PATH=' + conf.INSTALL_DIR + '/bin:\\\$PATH" >> ' + conf.INSTALL_DIR + '/bin/profile.sh')
			run('chmod a+x ' + conf.INSTALL_DIR + '/bin/profile.sh')
			run('ln -sf ' + conf.INSTALL_DIR + '/bin/profile.sh /etc/profile.d/')
		self.rm_pod()

	def install(self):
		run('touch /var/log/.install.log')

	def require(self):
		return ''

	def check(self):
		return self.test('/var/log/.install.log')

	# 删除pod2man 解决新系统机器openssl编辑出错问题
	# http://forums.gentoo.org/viewtopic-p-7392308.html
	def rm_pod(self):
		with quiet():
			output = run('which pod2man')
			if (output != ""):
				run('mv ' + output + ' ' + output + '.bak')

