#!/bin/bash

# 安装python
function install_python
{
	if [ -f $INSTALL_DIR/python/bin/python ]; then
		show_log "Python installed"
		return
	fi
	cd $DIST_DIR
	wget -c --no-check-certificate https://www.python.org/ftp/python/$PY_VERSION/Python-$PY_VERSION.tgz  | tee -a $LOG_FILE
	cd src
	tar zxf ../Python-$PY_VERSION.tgz
	cd Python-$PY_VERSION
	./configure --prefix=$INSTALL_DIR/python-$PY_VERSION  | tee -a $LOG_FILE
	make && make install  | tee -a $LOG_FILE
	ln -sf $INSTALL_DIR/python-$PY_VERSION $INSTALL_DIR/python
	show_log "Python installed"
}

# 安装easy_install
function install_ez
{
	if [ -f $INSTALL_DIR/python/bin/easy_install ]; then
		show_log "Easy_install installed"
		return
	fi
	cd $DIST_DIR
	wget -c --no-check-certificate https://bootstrap.pypa.io/ez_setup.py  | tee -a $LOG_FILE
	$INSTALL_DIR/python/bin/python ez_setup.py  | tee -a $LOG_FILE
	show_log "Easy_install installed"
}

# 安装fab
function install_fab
{
	if [ -f $INSTALL_DIR/python/bin/fab ]; then
		show_log "Fabric installed"
		return
	fi
	$INSTALL_DIR/python/bin/easy_install fabric  | tee -a $LOG_FILE
	show_log "Fabric installed"
}

# 安装pip
function install_pip
{
	if [ -f $INSTALL_DIR/python/bin/pip ]; then
		show_log "Pip installed"
		return
	fi
	cd $DIST_DIR
	wget -c --no-check-certificate https://bootstrap.pypa.io/get-pip.py  | tee -a $LOG_FILE
	$INSTALL_DIR/python/bin/python get-pip.py  | tee -a $LOG_FILE
	show_log "Pip installed"
}

# 打印信息
function show_log {
	local datetime=$(date "+%F %T")
	echo "$datetime $@" >> $LOG_FILE
	    
	msg=$(echo $@ | sed "s/\(.*error.*\)/\\\e[31m\1\\\e[0m/ig")
	msg=$(echo $msg | sed "s/\(.*installed.*\)/\\\e[32m\1\\\e[0m/ig")
	echo -e $msg
}

# 包含系统命令
function source_system
{
	os=`head -n 1 /etc/issue|cut -d" " -f1|tr '[A-Z]' '[a-z]'`
	case "$os" in
		"debian" | "ubuntu" )
			source $SHELL_DIR/debian.sh
			;;
		"redhat" | "centos" | "fedora" )
			source $SHELL_DIR/redhat.sh
			;;
		"arch")
			source $SHELL_DIR/arch.sh
			;;
		"gentoo")
			source $SHELL_DIR/gentoo.sh
			;;
		"")
			show_log "System not support! Exit." && exit 1
	esac
}

