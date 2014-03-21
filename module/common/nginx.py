# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
from core.utils import utils
class nginx(base):
	def install(self):
		self.download(conf.NGINX_URL + '/' + conf.NGINX + '.tar.gz')
		self.unzip(conf.NGINX)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.NGINX):
			run('''
				./configure --prefix=''' + conf.INSTALL_DIR + '''/opt/nginx \
				--with-http_ssl_module \
				--with-http_stub_status_module \
				--with-http_realip_module \
				--http-client-body-temp-path=''' + conf.INSTALL_DIR + '''/opt/nginx/temp/client-body \
				--http-proxy-temp-path=''' + conf.INSTALL_DIR + '''/opt/nginx/temp/proxy \
				--http-fastcgi-temp-path=''' + conf.INSTALL_DIR + '''/opt/nginx/temp/fastcgi \
				--http-uwsgi-temp-path=''' + conf.INSTALL_DIR + '''/opt/nginx/temp/uwsgi \
				--http-scgi-temp-path=''' + conf.INSTALL_DIR + '''/opt/nginx/temp/scgi
			''')
			run("make && make install")
			run('mkdir -p ' + conf.INSTALL_DIR + '/opt/nginx/temp')
			run('mkdir -p ' + conf.INSTALL_DIR + '/opt/nginx/conf/vhosts')
			run('mkdir -p ' + conf.INSTALL_DIR + '/app/app_default/wwwroot')
			run('cp -rf conf/nginx/conf/* ' + conf.INSTALL_DIR + '/opt/nginx/conf/')
		self.chkconfig('nginx')
		self.path('nginx')
		utils().adduser('www')
		run('cp ' + conf.BASE_DIR + '/conf/nginx/nginx_cut_log.sh ' + conf.INSTALL_DIR + '/bin/')
		run('chmod a+x ' + conf.INSTALL_DIR + '/bin/nginx_cut_log.sh')
		cpu = run('cat /proc/cpuinfo | grep processor | wc -l')
		run('sed -i "s/<worker_processes>/' + cpu + '/" ' + conf.INSTALL_DIR + '/opt/nginx/conf/nginx.conf')

	def require(self):
		str = base.require(self)
		return str + ',pcre'

	def check(self):
		with quiet():
			output = run('test -e ' + conf.INSTALL_DIR + '/opt/nginx;echo $?')
			return output
