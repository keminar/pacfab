#!/usr/bin/python
# encoding: utf-8

import os
import sys
import conf
from fabric.api import *

def install_mysql():
	with cd(conf.BASE_DIR + '/dist'):
		run('wget -c ' + conf.MIRROR + '/mysql/MySQL-5.5/' + conf.MYSQL + '.tar.gz')
	with cd(conf.BASE_DIR + '/src'):
		run('tar zxf ../dist/' + conf.MYSQL + '.tar.gz')
	with cd(conf.BASE_DIR + '/src/' + conf.MYSQL):
		run('''
			cmake . -DCMAKE_INSTALL_PREFIX=''' + conf.INSTALL_DIR + '''/opt/mysql \
			-DMYSQL_UNIX_ADDR=''' + conf.INSTALL_DIR + '''/srv/mysql/3306/mysql.sock \ 
			-DWITH_INNOBASE_STORAGE_ENGINE=1 \
			-DMYSQL_TCP_PORT=3306 -DEXTRA_CHARSETS=all \
			-DDEFAULT_CHARSET=utf8 \
			-DDEFAULT_COLLATION=utf8_general_ci \
			-DWITH_DEBUG=0
		''')
		run('make && make install')
		run('groupadd -f mysql')
		run('useradd -g mysql mysql', warn_only=True)

def config_mysql(port='3306'):
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
