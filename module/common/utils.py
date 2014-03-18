# encoding: utf-8

from fabric.api import *

def os_release():
	with quiet():
		output = run('head -n 1 /etc/issue|cut -d" " -f1')
		return output.lower()

def os_module():
	os = os_release()
	if (os == 'debian' or os == 'ubuntu'):
		return 'module.debian'
	elif(os == 'redhat' or os == 'centos' or os == 'fedora'):
		return 'module.redhat'
	else:
		raise Exception("不支持的操作系统")
