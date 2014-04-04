#!/bin/bash

# 编译环境
function install_build
{
	pacman -S base-devel --noconfirm --need
	show_log "Build environment installed"
}
