#!/usr/bin/python
# encoding: utf-8

#http://docs.fabfile.org/en/1.8/tutorial.html
from fabric.api import *
from plugin.php import *
from plugin.mysql import *
from plugin.cmake import *
from plugin.apache import *
from plugin.nginx import *

env.user = 'root'
env.roledefs = {
	'host': ['root@192.168.1.33:22']
}
env.password = 'cwv0g4ot'

@parallel
def php():
	install_php()

@parallel
def mysql():
	install_cmake()
	install_mysql()
	config_mysql()

@parallel
def mysql_instance(port="3306"):
	config_mysql(port)

@parallel
def apache():
	install_apr()
	install_openssl()
	install_apache()

@parallel
def nginx():
	install_pcre()
	install_nginx()

@roles('host')
@parallel
def lamp():
	mysql()
	apache()
	php()
	nginx()
