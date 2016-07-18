#!/bin/bash

# 编译环境
function install_build
{
	apt-get install build-essential libssl-dev
	show_log "Build environment installed"
}
