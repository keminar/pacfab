install
=======
一键安装多机LAMP等软件环境

安装说明
-------
		./setup.sh -H localhost -u root -p password install:name=anmp
		说明name值为要安装的软件
支持的软件
-------
		apache              [apache]
		git                 [git]
		nginx               [nginx]
		mysql               [mysql]
		int                 [int system]
		anmp                [apache nginx mysql php]
		php                 [php]
		vim                 [vim config]

安装实例
-------
		./setup.sh -H localhost -u root -p password instance:name=mysql,port=3307
		说明name值为要配置实例的软件,port为新实例的端口
支持的软件
		MYSQL

指定一组机器
-------
		./setup.sh -H localhost1,loclahost2 -u root -p password install:name=namp

更多参数
-------
		./setup.sh 查看帮助

本机免密码快捷方式
------
		./local.sh install:anmp
