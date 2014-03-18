# encoding: utf-8

import conf
from fabric.api import *

class base(object):

	def unzip(self, name, ext = '.tar.gz'):
		with cd(conf.BASE_DIR + '/dist/src'):
			run('tar zxf ../' + name + ext)

	def download(self, url):
		with cd(conf.BASE_DIR + '/dist'):
			run('wget -c ' + url)
