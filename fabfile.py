# encoding: utf-8

import os
import sys
import importlib
import conf
from fabric.api import *
from module.common.utils import *

@parallel
def install(name = ""):
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

		# check
		func = getattr(initClass, 'check')
		code = func()
		if (code == "0"):
			print("\"%s\" has been installed" % name)
			return
		
		# require
		func = getattr(initClass, 'require')
		require = func()
		for r in require.split(","):
			if (r != ""):
				install(r)

		# install
		func = getattr(initClass, 'install')
		Code = func()
	else:
		usage()

@parallel
def instance(name = "", port = ""):
	if (name != "" and port !=""):
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

		# instance
		func = getattr(initClass, 'instance')
		code = func(port)
	else:
		usage()

# 用户帮助提示参数
def usage():
	paramMap = {
		"int"    :"int system",
		"anmp"   :"apache nginx mysql php",
		"php"    :"php",
		"apache" :"apache",
		"mysql":"mysql",
		"nginx":"nginx",
		"git"  : "git",
		"vim"  : "vim config",
	}
	print("Please input soft name")
	print("Softname:")
	for soft in paramMap:
		print("\t%-20s[%s]" % (soft, paramMap[soft]))
