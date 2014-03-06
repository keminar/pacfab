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
			--with-config-file-path=''' + conf.INSTALL_DIR + '''/opt/php/etc \
			--with-apxs2=''' + conf.INSTALL_DIR + '''/opt/apache/bin/apxs \
			--with-openssl \
			--with-readline \
			--enable-pcntl \
			--enable-bcmath \
			--enable-calendar \
			--enable-fpm \
			--with-mysql=''' + conf.INSTALL_DIR + '''/opt/mysql \
			--with-mysqli=''' + conf.INSTALL_DIR + '''/opt/mysql/bin/mysql_config \
			--with-pdo-mysql=''' + conf.INSTALL_DIR + '''/opt/mysql \
			--enable-pdo \
			--with-gettext \
			--enable-mbstring \
			--with-mhash \
			--with-mcrypt \
			--with-gd \
			--with-jpeg-dir \
			--with-png-dir \
			--with-freetype-dir \
			--enable-gd-native-ttf \
			--enable-exif \
			--with-curl \
			--with-curlwrappers \
			--with-ldap \
			--with-ldap-sasl \
			--with-xmlrpc \
			--enable-soap \
			--enable-sockets \
			--enable-ftp \
			--with-bz2 \
			--with-zlib \
			--enable-zip
		''')
		run("make ZEND_EXTRA_LIBS='-liconv' && make install")
