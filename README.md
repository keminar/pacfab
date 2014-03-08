install
=======
一键安装多机LAMP等软件环境

使用说明
-------
先使用init.sh安装fabfile环境，然后使用fab命令安装软件

初始化系统
-------
fab init

安装LAMP
-------
		fab mysql
		fab apache
		fab php
安装MYSQL实例
-------
		fab mysql_instance:port=3307

指定一组机器
-------
		fab -R host lamp
