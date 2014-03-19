# encoding: utf-8

import conf
from fabric.api import *

class base(object):

	def unzip(self, name, ext = '.tar.gz'):
		with cd(conf.BASE_DIR + '/dist/src'):
			run('gunzip -q < ../' + name + ext + ' | tar xf -')

	def download(self, url):
		with cd(conf.BASE_DIR + '/dist'):
			run('wget -c ' + url)

	def require(self):
		return 'init'
	
	def check(self):
		return 0

	def instance(self, port):
		pass
