# encoding: utf-8

import conf
from fabric.api import *
from core.utils import utils
from module.common.init import init
class init(init):
        def install(self):
                with quiet():
                        if (run('grep "/etc/profile.d" /etc/profile') == ""):
                                put(conf.BASE_DIR + '/conf/init/profile.tpl', conf.BASE_DIR)
                                run('cat ' + conf.BASE_DIR + '/profile.tpl >> /etc/profile')
                run('emerge -n libjpeg-turbo libpng libXpm freetype libxslt cyrus-sasl')
                run('emerge -n curl wget openldap')
                run('emerge -n ncurses libxml2 zlib bzip2 readline')

                super(init, self).install()
