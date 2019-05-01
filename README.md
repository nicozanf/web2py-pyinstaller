# web2py-pyinstaller 
How to make web2py Windows & Macintosh binaries with python 2 / 3 and pyinstaller 

**********************************************************************************
Please, help with testing. Write the results directly to me (nicozanf@gmail.com)   
**********************************************************************************  
  
## Problem: 
web2py has Windows and Macintosh binaries made with py2exe and later with bbfreeze (see [Niphlod's page](http://www.web2pyslices.com/slice/show/1726/build-windows-binaries) ). Unfortunately, while web2py nowadays runs fine with pyhton 3.5+ these build tools are not currently compatible with python >= 3.5.  
Hence I've started to look for alternatives, and after some work I've succeeded to gain 64 bit binaries using Pyinstaller.

Here you can find the experimental binary for MacOs and Windows, build by me with python 3.7 but also with python 2.7 if you still use it.

If you prefer to build them by yourself, see the specific README [for Windows](https://github.com/nicozanf/web2py-pyinstaller/blob/master/README_win.md) and [for Mac](https://github.com/nicozanf/web2py-pyinstaller/blob/master/README_mac.md).


Also, there is [a simple HOWTO](https://github.com/nicozanf/web2py-pyinstaller/blob/master/HOWTO-modules.md) that shows how to install additional modules directly on the binaries. 
