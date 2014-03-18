#!/usr/bin/python
# encoding: utf-8

import conf
from fabric.api import *
from module.common.base import base
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
			run('groupadd -f mysql')
			run('useradd -g mysql mysql', warn_only=True)

	def config(self, port = '3306'):
		run('mkdir -p ' + conf.INSTALL_DIR + '/srv/mysql/' + port + '/data')
		run('chown -R mysql:mysql ' + conf.INSTALL_DIR + '/srv/mysql/' + port)
		with cd(conf.INSTALL_DIR + '/opt/mysql'):
			run('''
				./scripts/mysql_install_db \
				--basedir=''' + conf.INSTALL_DIR + '''/opt/mysql \
				--datadir=''' + conf.INSTALL_DIR + '''/srv/mysql/''' + port + '''/data --user=mysql
			''')
			run('cp support-files/mysql.server ' + conf.INSTALL_DIR + '/bin/mysql.init')
			run('cp support-files/my-large.cnf ' + conf.INSTALL_DIR + '/srv/mysql/' + port + '/my.cnf')
			run('chmod +x ' + conf.INSTALL_DIR + '/bin/mysql.init')
	def require(self):
		return 'cmake'
