#!/usr/bin/python
# encoding: utf-8

#http://docs.fabfile.org/en/1.8/tutorial.html
from fabric.api import *
from plugin.php import *
from plugin.mysql import *
from plugin.cmake import *
from plugin.apache import *

env.roledefs = {
	'host': ['root@192.168.1.33:22']
}
env.password = 'cwv0g4ot'

@roles('host')
@parallel
def php():
	install_php()

@roles('host')
@parallel
def mysql():
	install_cmake()
	install_mysql()
	config_mysql()

@roles('host')
@parallel
def mysql_instance():
	config_mysql()

@roles('host')
@parallel
def apache():
	install_apr()
	install_openssl()
	install_apache()

