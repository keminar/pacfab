install
=======
一键安装多机LAMP环境

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
