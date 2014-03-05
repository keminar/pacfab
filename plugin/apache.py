#!/usr/bin/python
# encoding: utf-8

import os
import sys
import conf
from fabric.api import *

def install_apr():
	with cd(conf.BASE_DIR + '/dist'):
		run('wget -c ' + conf.APACHE_URL + '/apr/' + conf.APR + '.tar.gz')
	with cd(conf.BASE_DIR + '/src'):
		run('tar zxf ../dist/' + conf.APR + '.tar.gz')
	with cd(conf.BASE_DIR + '/src/' + conf.APR):
		run('''
			./configure --prefix=/usr/local/apr && \
			make && make install
		''')
	with cd(conf.BASE_DIR + '/dist'):
		run('wget -c ' + conf.APACHE_URL + '/apr/' + conf.APR_UTIL + '.tar.gz')
	with cd(conf.BASE_DIR + '/src'):
		run('tar zxf ../dist/' + conf.APR_UTIL + '.tar.gz')
	with cd(conf.BASE_DIR + '/src/' + conf.APR_UTIL):
		run('''
			./configure --prefix=/usr/local/apr-util --with-apr=/usr/local/apr &&\
			make && make install
		''')

def install_openssl():
	with cd(conf.BASE_DIR + '/dist'):
		run('wget -c ' + conf.OPENSSL_URL + '/source/' + conf.OPENSSL + '.tar.gz')
	with cd(conf.BASE_DIR + '/src'):
		run('tar zxf ../dist/' + conf.OPENSSL + '.tar.gz')
	with cd(conf.BASE_DIR + '/src/' + conf.OPENSSL):
		run('''
			./config --prefix=/usr/local --openssldir=/usr/local/ssl &&\
			make && make install
		''')

def install_apache():
	with cd(conf.BASE_DIR + '/dist'):
		run('wget -c ' + conf.MIRROR + '/apache/' + conf.APACHE + '.tar.gz')
	with cd(conf.BASE_DIR + '/src'):
		run('tar zxf ../dist/' + conf.APACHE + '.tar.gz')
	with cd(conf.BASE_DIR + '/src/' + conf.APACHE):
		run('''
			./configure  --prefix=''' + conf.INSTALL_DIR + '''/opt/apache \
			--enable-so --enable-ssl --with-ssl=/usr/local/ssl \
			--enable-rewrite \
			--enable-module=most \
			--with-apr=/usr/local/apr \
			--with-apr-util=/usr/local/apr-util/ \
			--disable-ipv6
		''')
		run('make && make install')
