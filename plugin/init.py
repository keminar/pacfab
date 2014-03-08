#!/usr/bin/python
# encoding: utf-8

import os
import sys
import conf
from fabric.api import *

def install_init():
	run('mkdir -p ' + conf.INSTALL_DIR + '/{bin,opt,srv}')
	run('mkdir -p ' + conf.BASE_DIR + '/{dist,src}')
	run('apt-get update')
	run('apt-get install -y build-essential')
	run('apt-get install -y libncurses5-dev libxml2-dev zlib1g-dev libbz2-dev libmcrypt-dev libreadline-dev')
	run('apt-get intsall -y libcurl4-gnutls-dev libjpeg-dev libpng-dev libxpm-dev libfreetype6-dev libxslt1-dev libsasl2-dev')
