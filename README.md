# web2py-pyinstaller 
How to make web2py Windows & Macintosh binaries with python 2 / 3 and pyinstaller 

*********************************************
Please, help with testing and report any bug
*********************************************

## Which version should you use?

The recommended versions for new users are:

- web2py_win_2191_py374.zip for Windows  (web2py 2.19.1 and python 3.7.4)
- web2py_osx_2191_py374.zip for MacOs (web2py 2.19.1 and python 3.7.4)

Use Python 2 only if you need to use old existing apps, while web2py version 3.x is experimental and unstable.

## Module HOWTO
Also, there is [a simple HOWTO](https://github.com/nicozanf/web2py-pyinstaller/blob/master/HOWTO-modules.md) that shows how to install additional modules directly on the binaries.   
  
## History: 
web2py has Windows and Macintosh binaries made with py2exe and later with bbfreeze (see [Niphlod's page](http://www.web2pyslices.com/slice/show/1726/build-windows-binaries) ). Unfortunately, while web2py nowadays runs fine with pyhton 3.5+ these build tools are not currently compatible with python >= 3.5.  
Hence I've started to look for alternatives, and after some work I've succeeded to gain 64 bit binaries using [Pyinstaller](https://github.com/pyinstaller/pyinstaller).

Here you can find the experimental binary for MacOs and Windows, build by me with python 3.7 but also with python 2.7 if you still use it.

If you prefer to build them by yourself, see the specific README [for Windows](https://github.com/nicozanf/web2py-pyinstaller/blob/master/README_win.md) and [for Mac](https://github.com/nicozanf/web2py-pyinstaller/blob/master/README_mac.md).


