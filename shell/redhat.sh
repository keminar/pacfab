#!/bin/bash

# 编译环境
function install_build
{
	yum install gcc gcc-c++ gcc-g77 flex bison autoconf automake bzip2-devel zlib-devel ncurses-devel libjpeg-devel libpng-devel libtiff-devel freetype-devel pam-devel openssl-devel libxml2-devel gettext-devel pcre-devel
	show_log "Build environment installed"
}
