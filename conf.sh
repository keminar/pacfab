#!/bin/bash

# 下载文件目录
readonly DIST_DIR=$SCRIPT_DIR/dist

# Libraries & functions
readonly SHELL_DIR=$SCRIPT_DIR/shell

# Runtime log output directory
readonly LOGS_DIR=$SCRIPT_DIR/logs

# Current log filename
readonly LOG_FILE=$LOGS_DIR/$(basename $SCRIPT).log

# Python软件安装目录
readonly INSTALL_DIR=/data/opt

# Python 版本
PY_VERSION=2.7.6
