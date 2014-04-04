install
=======
一键安装多机LAMP等软件环境

安装说明
-------
		./setup.sh -H localhost -u root -p password install:name=anmp
		说明name值为要安装的软件
支持的软件
-------
		pcre            [The PCRE library is a set of functions that implement regular expression pattern]
		iconv           [iconv is a computer program used to convert between different character encodings]
		git             [Git is a free and open source distributed version control system]
		cmake           [CMake is a family of tools designed to build, test and package software. ]
		mhash           [Libmhash is a library that provides a uniform interface to several hash algorithms.]
		int             [Int system]
		screen          [Screen is a full-screen window manager that multiplexes a physical terminal between several processes]
		redis           [Redis is an open source, BSD licensed, advanced key-value store.]
		openssl         [The OpenSSL Project is a collaborative effort to develop a general purpose cryptography library.]
		vim             [Vim is a highly configurable text editor built to enable efficient text editing]
		nginx           [nginx [engine x] is an HTTP and reverse proxy server]
		mysql           [The world's most popular open source database]
		apache          [The Apache HTTP Server Project is an effort to develop and maintain an open-source HTTP server]
		mcrypt          [mcrypt, and the accompanying libmcrypt, are intended to be replacements for the old Unix crypt]
		php             [PHP is a popular general-purpose scripting language]
		anmp            [apache nginx mysql php]
		apr             [Apache Portable Runtime (APR) project]

安装实例
-------
		./setup.sh -H localhost -u root -p password instance:name=mysql,port=3307
		说明name值为要配置实例的软件,port为新实例的端口
支持的软件
-------
		mysql           [The world's most popular open source database]
		redis           [Redis is an open source, BSD licensed, advanced key-value store.]

指定一组机器
-------
		./setup.sh -H localhost1,loclahost2 -u root -p password install:name=namp

更多参数
-------
		./setup.sh 查看帮助

本机免密码快捷方式
------
		./local.sh install:anmp
