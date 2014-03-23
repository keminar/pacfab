#!/usr/bin/python
# encoding: utf-8

import string
import re
import conf
from fabric.api import *
from core.base import base
from core.utils import utils
class mysql(base):
	def install(self):
		self.download(conf.MIRROR + '/mysql/MySQL-5.5/' + conf.MYSQL + '.tar.gz')
		self.unzip(conf.MYSQL)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.MYSQL):
			run('rm -f CMakeCache.txt')
			run('''cmake . -DCMAKE_INSTALL_PREFIX=''' + conf.INSTALL_DIR + '''/opt/mysql \
				-DSYSCONFDIR=''' + conf.INSTALL_DIR + '''/srv/mysql/3306 \
				-DMYSQL_DATADIR=''' + conf.INSTALL_DIR + '''/srv/mysql/3306/data \
				-DMYSQL_UNIX_ADDR=''' + conf.INSTALL_DIR + '''/srv/mysql/3306/mysql.sock \
				-DWITH_INNOBASE_STORAGE_ENGINE=1 \
				-DMYSQL_TCP_PORT=3306 \
				-DDEFAULT_CHARSET=utf8 \
				-DDEFAULT_COLLATION=utf8_general_ci \
				-DWITH_EXTRA_CHARSETS=complex \
				-DWITH_ARCHIVE_STORAGE_ENGINE=ON \
				-DWITH_EMBEDDED_SERVER=ON \
				-DENABLED_LOCAL_INFILE=ON \
				-DWITH_DEBUG=0
			''')
			run('make && make install')
		utils().adduser('mysql')
		self.chkconfig('mysql')
		self.path('mysql')
		self.instance()
		run('touch ' + conf.INSTALL_DIR + '/opt/mysql/.install.log')


	def instance(self, port = '3306'):
		mem = string.atoi(utils().mem())
		if ( mem >= 4000):
			mycnf = 'my-innodb-heavy-4G.cnf'
		elif (mem >= 1000):
			mycnf = 'my-huge.cnf'
		elif (mem >= 512):
			mycnf = 'my-large.cnf'
		elif (mem >= 128):
			mycnf = 'my-medium.cnf'
		else:
			mycnf = 'my-small.cnf'
		dstPath = conf.INSTALL_DIR + '/srv/mysql/' + port
		run('mkdir -p ' + dstPath + '/{data,binlogs}')
		with cd(conf.INSTALL_DIR + '/opt/mysql'):
			run('cp support-files/' + mycnf + ' ' + dstPath + '/my.cnf')
			run('sed -i "s/3306/' + port + '/g" ' + dstPath + '/my.cnf')
			with quiet():
				line = run("grep -n  '\[mysqld\]' " + dstPath + "/my.cnf |tail -n 1 | awk -F ':' '{print $1}'")
			run('sed -i "' + line + 'a\slow_query_log_file = ' + re.escape(dstPath + '/mysql-slow.log') + '" ' + dstPath + '/my.cnf')
			run('sed -i "' + line + 'a\log-bin = ' + re.escape(dstPath + '/binlogs/mysql-bin') + '" ' + dstPath + '/my.cnf')
			run('sed -i "' + line + 'a\log-error = ' + re.escape(dstPath + '/mysql-error.log') + '" ' + dstPath + '/my.cnf')
			run('sed -i "' + line + 'a\pid-file = ' + re.escape(dstPath + '/mysql.pid') + '" ' + dstPath + '/my.cnf')
			run('sed -i "' + line + 'a\datadir = ' + re.escape(dstPath + '/data') + '" ' + dstPath + '/my.cnf')
			run('sed -i "' + line + 'a\\basedir = ' + re.escape(conf.INSTALL_DIR + '/opt/mysql') + '" ' + dstPath + '/my.cnf')
			run('sed -i "' + line + 'a\user = mysql' + '" ' + dstPath + '/my.cnf')
			run('chown -R mysql:mysql ' + dstPath)
			run('''
				./scripts/mysql_install_db \
				--defaults-file=''' + conf.INSTALL_DIR + '''/srv/mysql/''' + port + '''/my.cnf
			''')
		run(conf.INSTALL_DIR + '/bin/mysql.init start ' + port)

	def require(self):
		str = base.require(self)
		return str + ',cmake'

	def check(self):
		return self.test(conf.INSTALL_DIR + '/opt/mysql/.install.log')
