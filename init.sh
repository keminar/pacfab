#!/bin/bash
apt-get update
apt-get install -y python
#wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
#python get-pip.py
wget -q http://peak.telecommunity.com/dist/ez_setup.py
python ez_setup.py

apt-get install -y gcc python-dev   libxml2 libxml2-dev  libxslt1.1 libxslt1-dev
easy_install fabric
