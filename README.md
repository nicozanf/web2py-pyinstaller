# web2py-pyinstaller 
How to make web2py Windows & Macintosh binaries with python 2 / 3 and pyinstaller 

**********************************************************************************
Please, help with testing. Write the results directly to me (nicozanf@gmail.com)   
**********************************************************************************  

## Which version for Mac?

The recommended version for new users is [web2py_osx.2_18_5.py3_cmd.zip](https://github.com/nicozanf/web2py-pyinstaller/blob/master/web2py_osx.2_18_5.py3_cmd.zip)

- the **CMD** versions are the Command ones (with Python 2 or 3), and they should work in any recent Mac. Just run the **web2py** program inside the compressed folder.
- the **APP** versions are the bundled Apps (still with Python 2 or 3). They are nicer but work fine only up to MacOs 10.13 (High Sierra).
Unfortunately, on MacOs 10.14+ Apple has changed the security settings and this has somehow broken them. If you still want to use the Apps, you can somehow do it by ctrl-open them or ctrl-Show Contents and then run Contents/MacOs/web2py. Also, I've noticed that downloading the program with Safari embed some kind of security restriction on the programs; it's better if you download them with the Terminal and wget or similar...


## Module HOWTO
Also, there is [a simple HOWTO](https://github.com/nicozanf/web2py-pyinstaller/blob/master/HOWTO-modules.md) that shows how to install additional modules directly on the binaries.   
  
## History: 
web2py has Windows and Macintosh binaries made with py2exe and later with bbfreeze (see [Niphlod's page](http://www.web2pyslices.com/slice/show/1726/build-windows-binaries) ). Unfortunately, while web2py nowadays runs fine with pyhton 3.5+ these build tools are not currently compatible with python >= 3.5.  
Hence I've started to look for alternatives, and after some work I've succeeded to gain 64 bit binaries using [Pyinstaller](https://github.com/pyinstaller/pyinstaller).

Here you can find the experimental binary for MacOs and Windows, build by me with python 3.7 but also with python 2.7 if you still use it.

If you prefer to build them by yourself, see the specific README [for Windows](https://github.com/nicozanf/web2py-pyinstaller/blob/master/README_win.md) and [for Mac](https://github.com/nicozanf/web2py-pyinstaller/blob/master/README_mac.md).


