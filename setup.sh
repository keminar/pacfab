#!/bin/bash


# Abort on any errors
set -e -u

# Get current script path
readonly SCRIPT=$(readlink -f $0)
readonly SCRIPT_DIR=$(dirname $SCRIPT)

# Setup basic directories
cd $SCRIPT_DIR
mkdir -p dist/src logs

# Include required libraries
source $SCRIPT_DIR/conf.sh
source $SHELL_DIR/util.sh

if [ ! -f $INSTALL_DIR/python/bin/fab ]; then
	source_system
	install_build
	install_python
	install_ez
	install_pip
	install_fab
fi
$INSTALL_DIR/python/bin/fab --colorize-errors "$@"
