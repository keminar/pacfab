# encoding: utf-8

import os
import sys
import importlib
import conf
from fabric.api import *
from module.common.utils import *

@parallel
def install(name = "", method = "install"):
	if (name != ""):
		moduleName = os_module() + '.' + name
		modulePath = moduleName.replace(".", "/") + '.py'
		if not os.path.exists(modulePath):
			moduleName = 'module.common.' + name
		try:
			module = importlib.import_module(moduleName)
		except:
			print("Software module \"%s\" not found!" % moduleName)
			sys.exit(1)
		instanceClass = getattr(module, name)
		initClass = instanceClass()
		require = ""
		for c in dir(initClass):
			if 'require' == c.lower():
				func = getattr(initClass, 'require')
				require = func()
				break
		for r in require.split(","):
			install(r)
		func = getattr(initClass, method)
		exitCode = func()
	else:
		print("Please input soft name")

