# encoding: utf-8

import conf
from fabric.api import *
from core.base import base
from core.utils import utils
class php(base):
	def install(self):
		self.bit = utils().bit()
		self.download(conf.MIRROR + '/php/' + conf.PHP + '.tar.gz')
		self.unzip(conf.PHP)
		with cd(conf.BASE_DIR + '/dist/src/' + conf.PHP):
			# fix php bug #54736
			if (self.bit == "64"):
				run('sed -i "s/#ifdef OPENSSL_NO_SSL2/#ifndef OPENSSL_NO_SSL2/g"  ext/openssl/xp_ssl.c');
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
			run('cp php.ini-production ' + conf.INSTALL_DIR + '/opt/php/etc/php.ini')
		with cd(conf.INSTALL_DIR + '/opt/php/etc'):
			run('cp php-fpm.conf.default php-fpm.conf')
			run('sed -i "s/nobody/www/g" php-fpm.conf')
		utils().adduser('www')
		self.chkconfig('php')
		self.path('php')

	def require(self):
		str = base.require(self)
		return str + ',openssl,mysql,iconv'

	def check(self):
		with quiet():
			output = run('test -e ' + conf.INSTALL_DIR + '/opt/php ;echo $?')
			return output
