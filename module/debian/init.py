# encoding: utf-8

import conf
from fabric.api import *
from module.common.init import init
class init(init):
	def install(self):
		run('apt-get update -y')
		run('apt-get install -y build-essential')
		run('apt-get install -y libncurses5-dev libxml2-dev zlib1g-dev libbz2-dev libmcrypt-dev libreadline-dev')
		run('apt-get install -y libcurl4-gnutls-dev libjpeg-dev libpng-dev libxpm-dev libfreetype6-dev libxslt1-dev libsasl2-dev')
		super(init, self).install()
