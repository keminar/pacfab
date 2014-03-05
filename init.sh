#!/bin/bash

BASE_DIR=/data/install
INSTALL_DIR=/data/test

DIST_DIR=dist
SRC_DIR=src

# 初始化系统
function init
{
	mkdir -p $INSTALL_DIR/{bin,opt,srv}
	mkdir -p $BASE_DIR/{$DIST_DIR,$SRC_DIR}

	apt-get update
	apt-get install -y build-essential
	apt-get install -y python python-dev 
	apt-get install -y libxml2 libxml2-dev libxslt1.1 libxslt1-dev 
}

# 安装easy_install
function install_ez
{
	cd $BASE_DIR/$DIST_DIR
	wget -q http://peak.telecommunity.com/dist/ez_setup.py
	python ez_setup.py
}

# 安装fab
function install_fab
{
	easy_install fabric
}

# 安装pip
function install_pip
{
	cd $BASE_DIR/$DIST_DIR
	wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
	python get-pip.py
}

init
install_ez
install_fab
