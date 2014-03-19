# encoding: utf-8

import conf
from fabric.api import *
from module.common.base import base
class git(base):
	def install(self):
		run('yum install -y git')
