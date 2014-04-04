# encoding: utf-8

import os
import sys
import conf
import core.utils as cu
from fabric.api import *

@parallel
def install(name = ""):
	if (name != ""):
		initClass = cu.utils().initClass(name)

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
		help()

@parallel
def instance(name = "", port = ""):
	if (name != "" and port !=""):
		initClass = cu.utils().initClass(name)

		# instance
		func = getattr(initClass, 'instance')
		code = func(port)
	else:
		help()

# 用户帮助提示参数
def help():
	paramMap = {
		"int"    : "Int system",
		"git"    : "Git is a free and open source distributed version control system",
		"screen" : "Screen is a full-screen window manager that multiplexes a physical terminal between several processes",
		"vim"    : "Vim is a highly configurable text editor built to enable efficient text editing",
		"anmp"   : "apache nginx mysql php",
		"apache" : "The Apache HTTP Server Project is an effort to develop and maintain an open-source HTTP server",
		"nginx"  : "nginx [engine x] is an HTTP and reverse proxy server",
		"mysql"  : "The world's most popular open source database",
		"php"    : "PHP is a popular general-purpose scripting language",
		"apr"    : "Apache Portable Runtime (APR) project",
		"cmake"  : "CMake is a family of tools designed to build, test and package software. ",
		"iconv"  : "iconv is a computer program used to convert between different character encodings",
		"mcrypt" : "mcrypt, and the accompanying libmcrypt, are intended to be replacements for the old Unix crypt",
		"mhash"  : "Libmhash is a library that provides a uniform interface to several hash algorithms.",
		"openssl": "The OpenSSL Project is a collaborative effort to develop a general purpose cryptography library.",
		"pcre"   : "The PCRE library is a set of functions that implement regular expression pattern",
		"redis"  : "Redis is an open source, BSD licensed, advanced key-value store.",
	}
	print("Usage: ./local.sh [option] install:name=[name]")
	print("Usage: ./local.sh [option] instance:name=[name],port=[port]")
	print("install:")
	for soft in paramMap:
		print("\t%-16s[%s]" % (soft, paramMap[soft]))

	print("instance:")
	print("\t%-16s[%s]" % ('mysql', paramMap['mysql']))
	print("\t%-16s[%s]" % ('redis', paramMap['redis']))
