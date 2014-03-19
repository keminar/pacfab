# encoding: utf-8

import conf
from fabric.api import *
from module.common.git import git
class git(git):
	def install(self):
		run('apt-get install -y git')
