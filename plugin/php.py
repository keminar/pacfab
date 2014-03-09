#!/usr/bin/python
# encoding: utf-8

import os
import sys
import conf
from fabric.api import *

def install_iconv():
	with cd(conf.BASE_DIR + '/dist'):
		run('wget -c ' + conf.GNU_URL + '/libiconv/' + conf.ICONV + '.tar.gz')
	with cd(conf.BASE_DIR + '/src'):
		run('tar zxf ../dist/' + conf.ICONV + '.tar.gz')
	with cd(conf.BASE_DIR + '/src/' + conf.ICONV):
		run('./configure --prefix=' + conf.INSTALL_DIR + '/opt/libiconv --enable-extra-encodings ')
		run('make && make install')
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
			--with-iconv=''' + conf.INSTALL_DIR + '''/opt/libiconv \
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
		run("make && make install")
