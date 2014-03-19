# encoding: utf-8

import conf
from fabric.api import *
from module.common.base import base
class nginx(base):
	def install(self):
		self.download(conf.NGINX_URL + '/' + conf.NGINX + '.tar.gz')
		self.unzip(conf.NGINX)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.NGINX):
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
	def require(self):
		return 'pcre'
	def check(self):
		with quiet():
			output = run('test -e ' + conf.INSTALL_DIR + '/opt/nginx;echo $?')
			return output
