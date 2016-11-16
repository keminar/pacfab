Building Python with SSL support (http://stackoverflow.com/questions/5937337/building-python-with-ssl-support-in-non-standard-location)

In top level Python2.7.11 source dir:

1. Change Modules/Setup.dist, Modules/Setup : Uncomment _ssl section, comment out _socket (no-op if it's already commented out), uncomment and set SSL appropriately (path to your new ssl lib/includes etc.)

    Note: Modules/Setup file does not exist initially but after first run it get's content from Modules/Setup.dist i believe. Make sure changes are reflected in here before every run.

2. Apply patch: http://gist.github.com/eddy-geek/9604982 (make distclean if previously ran make)

```
./configure --prefix=/data/opt/python2.7 --enable-shared
# modify: Makefile -> set svnversion to ""
make
make install
```
