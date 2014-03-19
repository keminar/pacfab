# encoding: utf-8

import conf
from fabric.api import *
from module.common.base import base
class git(base):

	def check(self):
		with quiet():
			output = run('which git >/dev/null 2>&1;echo $?')
			return output
