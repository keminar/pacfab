# encoding: utf-8

import os
import sys
import conf
from fabric.api import *
from core.utils import *

@parallel
def install(name = ""):
	if (name != ""):
		initClass = utils().initClass(name)

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
		initClass = utils().initClass(name)

		# instance
		func = getattr(initClass, 'instance')
		code = func(port)
	else:
		help()

# 用户帮助提示参数
def help():
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
