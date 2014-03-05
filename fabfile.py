#!/usr/bin/python
# encoding: utf-8

#http://docs.fabfile.org/en/1.8/tutorial.html
from fabric.api import *
from plugin.php import *
from plugin.mysql import *

env.roledefs = {
    'host': ['root@blog.linuxphp.org:32222']
}
env.password = '7dnu8ygh'

@roles('host')
@parallel
def php():
    install_php()

@roles('host')
@parallel
def mysql():
    install_mysql()
