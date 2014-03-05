#!/usr/bin/python
# encoding: utf-8

import os
import sys
import conf
from fabric.api import *

def install_php():
    run('mkdir -p ' + conf.BASE_DIR + '/dist')
    with cd(conf.BASE_DIR + '/dist'):
        run('wget -c ' + conf.MIRROR + '/php/' + conf.PHP + '.tar.gz')
        run('mkdir -p ' + conf.BASE_DIR + '/src')
    with cd(conf.BASE_DIR + '/src'):
        run('tar zxf ../dist/' + conf.PHP + '.tar.gz')
    with cd(conf.BASE_DIR + '/src/' + conf.PHP):
        run('''
            ./configure  --prefix=/data/opt/php 
            --with-apxs2=/data/opt/apache/bin/apxs 
            --enable-fpm 
            --enable-debug 
            --with-mysql=/data/opt/mysql 
            --with-mysqli=/data/opt/mysql/bin/mysql_config 
            --with-gd 
            --with-curl 
            --enable-pdo 
            --with-pdo-mysql 
            --with-openssl 
            --with-jpeg-dir 
            --with-png-dir 
            --with-zlib 
            --with-freetype-dir 
        ''')
        run('make && make install')
