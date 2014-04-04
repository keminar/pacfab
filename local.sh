#!/bin/bash

USER_SSH=/root/.ssh

if [ ! -f $USER_SSH/id_rsa.pub ];then
	ssh-keygen -t rsa -f $USER_SSH/id_rsa  -C '' -N '' -q
fi

if [ ! -f $USER_SSH/authorized_keys ];then
	cat $USER_SSH/id_rsa.pub >> $USER_SSH/authorized_keys
fi

./setup.sh -H localhost -u root -i $USER_SSH/id_rsa.pub "$@"
