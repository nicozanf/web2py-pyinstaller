# web2py-pyinstaller 
How to make web2py Windows & Macintosh binaries with python 2 / 3 and pyinstaller 

**********************************************************************************
Please, help with testing. Write the results directly to me (nicozanf@gmail.com)   
**********************************************************************************  

## Which version should you use?

The recommended version for new users is the one with Python 3 embedded. Use Python 2 only if you need to use old existing apps.

## MacOS execution problems

Unfortunately, on MacOs 10.12+ Apple has changed the security settings and this has somehow broken the bundles apps normal behaviour. If you face execution problems, please follow one of the following advices:

- 'control' + click on downloaded file and then 'open' it (confirm the warnings). Then move the file in Applications and run it from there.
-  download the files from another OS (Windows or Linux) and then use an USB key / drive in order to copy them to the Mac. This will not insert the security Extended Attribute onto them.
- after dowloading the app, on a Terminal go to that folder and run 'xattr -d com.apple.quarantine  web2py.app' in order to delete the security Extended Attribute

## Module HOWTO
Also, there is [a simple HOWTO](https://github.com/nicozanf/web2py-pyinstaller/blob/master/HOWTO-modules.md) that shows how to install additional modules directly on the binaries.   
  
## History: 
web2py has Windows and Macintosh binaries made with py2exe and later with bbfreeze (see [Niphlod's page](http://www.web2pyslices.com/slice/show/1726/build-windows-binaries) ). Unfortunately, while web2py nowadays runs fine with pyhton 3.5+ these build tools are not currently compatible with python >= 3.5.  
Hence I've started to look for alternatives, and after some work I've succeeded to gain 64 bit binaries using [Pyinstaller](https://github.com/pyinstaller/pyinstaller).

Here you can find the experimental binary for MacOs and Windows, build by me with python 3.7 but also with python 2.7 if you still use it.

If you prefer to build them by yourself, see the specific README [for Windows](https://github.com/nicozanf/web2py-pyinstaller/blob/master/README_win.md) and [for Mac](https://github.com/nicozanf/web2py-pyinstaller/blob/master/README_mac.md).


