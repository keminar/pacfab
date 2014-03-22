# encoding: utf-8

import re
import conf
from fabric.api import *
from core.utils import *

class base(object):

	# 解压
	def unzip(self, name, ext = '.tar.gz'):
		with cd(conf.BASE_DIR + '/dist/src'):
			run('gunzip -q < ../' + name + ext + ' | tar xf -')

	# 下载
	def download(self, url):
		with cd(conf.BASE_DIR + '/dist'):
			run('wget -c ' + url)

	# 必须优先安装
	def require(self):
		return 'init'

	# 检查是否安装, 0已安装
	def check(self):
		return "0"

	# 增加实例
	def instance(self, port):
		pass

	# 开机启动
	def chkconfig(self, name):
		put(conf.BASE_DIR + '/conf/' + name + '/' + name + '.init', conf.INSTALL_DIR + '/bin/')
		run('chmod +x ' + conf.INSTALL_DIR + '/bin/' + name + '.init')
		run('sed -i "s/<INSTALL_DIR>/' + re.escape(conf.INSTALL_DIR) + '/g"  ' + conf.INSTALL_DIR + '/bin/' + name + '.init')
		run('ln -sf ' + conf.INSTALL_DIR + '/bin/' + name + '.init /etc/init.d/' + name)
		with quiet(): # redhat
			output = run('which chkconfig >/dev/null 2>&1;echo $?')
		if (output == "0"):
			run('chkconfig --del ' + name)
			run('chkconfig --add ' + name)
			run('chkconfig --level 345 ' + name + ' on')
			return
		with quiet(): # debian
			output = run('which update-rc.d >/dev/null 2>&1;echo $?')
		if (output == "0"):
			run('update-rc.d -f ' + name + ' remove')
			run('update-rc.d ' + name + ' start 85 3 4 5 . stop 15 0 6 .')

	# 环境变量
	def path(self, name):
		BASEPATH = conf.INSTALL_DIR + '/opt/' + name
		PROFILE = conf.INSTALL_DIR + '/bin/profile.sh'
		run('sed -i "/##' + name + '##/d" ' + PROFILE)
		if (self.test(BASEPATH + '/bin') == "0"):
			run('echo "export PATH=' + BASEPATH + '/bin:\\\$PATH \t##' + name + '##" >> ' + PROFILE)
		if (self.test(BASEPATH + '/sbin') == "0"):
			run('echo "export PATH=' + BASEPATH + '/sbin:\\\$PATH \t##' + name + '##" >> ' + PROFILE)

	# 文件是否存在
	def test(self, file):
		with quiet():
			return run('test -e ' + file + ';echo $?')
