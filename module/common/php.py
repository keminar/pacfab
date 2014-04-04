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
			# https://bugs.php.net/bug.php?id=54736
			if (self.bit == "64"):
				run('sed -i "s/#ifdef OPENSSL_NO_SSL2/#ifndef OPENSSL_NO_SSL2/g"  ext/openssl/xp_ssl.c');
			with_apache = ''
			if (self.test(conf.INSTALL_DIR + '/opt/apache') == '0'):
				with_apache = '--with-apxs2=' + conf.INSTALL_DIR + '/opt/apache/bin/apxs'
			run('''
				./configure  --prefix=''' + conf.INSTALL_DIR + '''/opt/php \
				--with-config-file-path=''' + conf.INSTALL_DIR + '''/opt/php/etc \
				''' + with_apache + ''' \
				--with-openssl=''' + conf.INSTALL_DIR + '''/opt/ssl \
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
				--with-mhash='''  + conf.INSTALL_DIR + '''/opt/hash \
				--with-mcrypt='''  + conf.INSTALL_DIR + '''/opt/mcrypt \
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
			self.patch()
			run("make && make install")
			run('cp php.ini-production ' + conf.INSTALL_DIR + '/opt/php/etc/php.ini')
		put(conf.BASE_DIR + '/conf/php/php-fpm.conf', conf.INSTALL_DIR + '/opt/php/etc/php-fpm.conf')
		utils().adduser('www')
		self.service('php')
		self.path('php')
		run(conf.INSTALL_DIR + '/bin/php.init start')
		self.apache()
		run('touch ' + conf.INSTALL_DIR + '/opt/php/.install.log')

	# ldap 部分机器编译解决方案
	# http://blog.chinaunix.net/uid-20776139-id-3631380.html
	def patch(self):
		with quiet():
			output = run('find /usr/lib/ -name "liblber-*"')
		if (output != ""):
			run("sed -i 's/^\(EXTRA_LIBS =.*\)$/\\1 -llber/' Makefile")

	def apache(self):
		if (self.test(conf.INSTALL_DIR + '/opt/apache') == "1"):
			return
		with quiet():
			line = run("grep -n  '#AddHandler cgi-script .cgi' " + conf.INSTALL_DIR + "/opt/apache/conf/httpd.conf |tail -n 1 | awk -F ':' '{print $1}'")
		run('sed -i "' + line + 'a\    AddHandler application\/x-httpd-php .php" ' + conf.INSTALL_DIR + '/opt/apache/conf/httpd.conf')
		run(conf.INSTALL_DIR + '/bin/apache.init start')

	def require(self):
		str = base.require(self)
		return str + ',openssl,mysql,iconv,mcrypt'

	def check(self):
		return self.test(conf.INSTALL_DIR + '/opt/php/.install.log')
