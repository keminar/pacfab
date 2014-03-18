install
=======
一键安装多机LAMP等软件环境

使用说明
-------
		./setup.sh install:name=anmp

初始化系统
-------
		./setup.sh install:name=init

安装ANMP
-------
		./setup.sh install:name=mysql
		./setup.sh install:name=nginx
		./setup.sh install:name=php
		./setup.sh install:name=apache
安装MYSQL实例
-------
		./setup.sh install:name=mysql,method=instance,port=3307

指定一组机器
-------
		fab -H localhost1,loclahost2 -p install:name=namp
