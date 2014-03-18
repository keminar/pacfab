#!/bin/bash

# 编译环境
function install_build
{
	apt-get install build-essential
	show_log "Build environment installed"
}
