#!/usr/bin/python
# encoding: utf-8

import os
import sys
import conf
from fabric.api import *
def install_mysql():
    run('mkdir -p ' + conf.BASE_DIR + '/dist')
    with cd(conf.BASE_DIR + '/dist'):
        run('wget -c ' + conf.MIRROR + '/mysql/MySQL-5.5/' + conf.MYSQL + '.tar.gz')
        run('mkdir -p ' + conf.BASE_DIR + '/src')
    with cd(conf.BASE_DIR + '/src'):
        run('tar zxf ../dist/' + conf.MYSQL + '.tar.gz')
    with cd(conf.BASE_DIR + '/src/' + conf.MYSQL):
        run('''
            cmake . -DCMAKE_INSTALL_PREFIX=/data/opt/mysql  \
            -DMYSQL_UNIX_ADDR=/data/srv/mysql/3306/mysql.sock \
            -DWITH_INNOBASE_STORAGE_ENGINE=1 \
            -DMYSQL_TCP_PORT=3306 -DEXTRA_CHARSETS=all \
            -DDEFAULT_CHARSET=utf8 \
            -DDEFAULT_COLLATION=utf8_general_ci \
            -DWITH_DEBUG=0
        ''')
        #run('make && make install')
