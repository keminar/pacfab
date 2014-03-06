#!/usr/bin/python
# encoding: utf-8

import os
import sys
import conf
from fabric.api import *

def install_php():
	with cd(conf.BASE_DIR + '/dist'):
		run('wget -c ' + conf.MIRROR + '/php/' + conf.PHP + '.tar.gz')
	with cd(conf.BASE_DIR + '/src'):
		run('tar zxf ../dist/' + conf.PHP + '.tar.gz')
	with cd(conf.BASE_DIR + '/src/' + conf.PHP):
		run('''
			./configure  --prefix=''' + conf.INSTALL_DIR + '''/opt/php \
			--with-apxs2=''' + conf.INSTALL_DIR + '''/opt/apache/bin/apxs \
			--enable-fpm \
			--enable-debug \
			--with-mysql=''' + conf.INSTALL_DIR + '''/opt/mysql \
			--with-mysqli=''' + conf.INSTALL_DIR + '''/opt/mysql/bin/mysql_config \
			--with-gd \
			--with-curl \
			--enable-pdo \
			--with-pdo-mysql \
			--with-openssl \
			--with-jpeg-dir \
			--with-png-dir \
			--with-zlib \
			--with-freetype-dir 
		''')
		run("make ZEND_EXTRA_LIBS='-liconv' && make install")
