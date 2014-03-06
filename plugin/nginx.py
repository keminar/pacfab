#!/usr/bin/python
# encoding: utf-8

import os
import sys
import conf
from fabric.api import *

def install_pcre():
	with cd(conf.BASE_DIR + '/dist'):
		run('wget -c ' + conf.PCRE_URL + conf.PCRE + '.tar.gz')
	with cd(conf.BASE_DIR + '/src'):
		run('tar zxf ../dist/' + conf.PCRE + '.tar.gz')
	with cd(conf.BASE_DIR + '/src/' + conf.PCRE):
		run('./configure && make && make install')

def install_nginx():
	with cd(conf.BASE_DIR + '/dist'):
		run('wget -c ' + conf.NGINX_URL + conf.NGINX + '.tar.gz')
	with cd(conf.BASE_DIR + '/src'):
		run('tar zxf ../dist/' + conf.NGINX + '.tar.gz')
	with cd(conf.BASE_DIR + '/src/' + conf.NGINX):
		run('''
			./configure  --prefix=''' + conf.INSTALL_DIR + '''/opt/nginx \
			--with-http_stub_status_module \
			--with-http_realip_module \
			--http-client-body-temp-path=''' + conf.INSTALL_DIR + '''/opt/nginx/temp/client-body \
			--http-proxy-temp-path=''' + conf.INSTALL_DIR + '''/opt/nginx/temp/proxy \
			--http-fastcgi-temp-path=''' + conf.INSTALL_DIR + '''/opt/nginx/temp/fastcgi \
			--http-uwsgi-temp-path=''' + conf.INSTALL_DIR + '''/opt/nginx/temp/uwsgi \
			--http-scgi-temp-path=''' + conf.INSTALL_DIR + '''/opt/nginx/temp/scgi
		''')
		run('mkdir -p ' + conf.INSTALL_DIR + '/opt/nginx/temp')
		run("make && make install")
