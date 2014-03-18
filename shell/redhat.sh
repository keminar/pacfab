#!/bin/bash

# 编译环境
function install_build
{
	yum install groupinstall "Development tools"
	show_log "Build environment installed"
}
