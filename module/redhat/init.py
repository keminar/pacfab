# encoding: utf-8

import conf
from fabric.api import *
from module.common.init import init
class init(init):
	def install(self):
		run('yum update -y')
		run('yum install -y gcc gcc-c++ gcc-g77 flex bison autoconf automake ncurses-devel')
		run('yum install -y bzip2-devel zlib-devel libjpeg-devel libpng-devel libtiff-devel freetype-devel gettext-devel')
		run('yum install -y pam-devel openssl-devel libxml2-devel pcre-devel libcurl-devel openldap-devel readline-devel')
		run('cp -frp /usr/lib64/libldap* /usr/lib/')
		run('rpm -ivh "http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm"')
		run('yum install -y --nogpgcheck libmcrypt-devel')
