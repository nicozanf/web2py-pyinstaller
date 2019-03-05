# web2py-pyinstaller 
How to make web2py windows binaries with python 3 and pyinstaller 

*****************************************************************************************************************  
* Please, help with testing. Write the results directly on https://github.com/nicozanf/web2py-pyinstaller/wiki   
*****************************************************************************************************************  
  
## Problem: 
web2py has Windows binaries made with py2exe and later with bbfreeze (see Niphlod's page on http://www.web2pyslices.com/slice/show/1726/build-windows-binaries). Unfortunately, while web2py nowadays runs fine with pyhton 3.5+ these build tools are not currently compatible with python >= 3.5.  
Hence I've started to look for alternatives, and after some work I've succeeded to gain 64 bit binaries using Pyinstaller.



## Full recipe:
1. get a clean Windows 10 (Windows 10 Professional English build 1809 64 bit, under Virtualbox in my case)
2. grab and install the official Python installer: I've got version 3.7.2, 64 bit  (https://www.python.org/ftp/python/3.7.2/python-3.7.2-amd64.exe ) + select  "add Python 3.7 to PATH" during its setup
3. update tools with  
"python -m pip install --upgrade pip"  --> pip-19.0.3  
"pip install --upgrade setuptools" --> setuptools-40.8.0-py2.py3-none-any.whl
4. install python-win32, which is needed for web2py to work with all features enabled (https://github.com/mhammond/pywin32/releases/download/b224/pywin32-224.win-amd64-py3.7.exe)
5. grab latest web2py source from https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip (you need at least 2.18.3 for needed changes in gluon.admin.py). Unzip it in a dedicated folder, in this example C:\web2py - so that you have C:\web2py\web2py.py inside)
6. install PyInstaller with:  
        pip install pyinstaller  (I've got PyInstaller-3.4.tar.gz )  
7. install the free Microsoft Visual C++ Redistributable per Visual Studio 2017, 64 bit version, from https://aka.ms/vs/15/release/vc_redist.x64.exe . Install it.
8. additional (but not required) packages to work better in the Windows world:  
pip install psycopg2 = psycopg2-2.7.7-cp37-cp37m-win_amd64.whl  
pip install pyodbc = pyodbc-4.0.26-cp37-cp37m-win_amd64.whl  
pip install ldap3 = ldap3-2.5.2-py2.py3-none-any.whl + pyasn1-0.4.5-py2.py3-none-any.whl  

9. copy the modified setup_exe.py from this repository to C:\web2py\setup_exe.py. Also copy C:\web2py\extras\build_web2py\setup_exe.conf to C:\web2py\setup_exe.conf
10. open a CMD and go to C:\web2py. Run:

    python setup_exe.py pyinstaller

If everything goes fine, you'll obtain the 64 bit binary build zipped as C:\web2py\web2py_win.zip.
If you try to run it in a 32 bit Windows system, you'll correctly get a 'web2py.exe not a valid Win32 application' error message.

## Gothca:
- in the console sometimes I've got many non-stopping errors like 'ERROR:Rocket.Errors.Thread-2:Tried to send "500 Server Error" to client but received socket error'. They disappear as soon as I've disabled IPv6 and rebooted. There are users that report also to fix similar problems by adding the hostname on the hosts file
- psycopg2 is placed in a folder by itself, instead than in the root folder
- in the currently officially binary build (with pyhton 2.7) there are also two binaries: web2py_no_console.exe and web2py_on_gevent.exe. They don't run correctly, and don't seem to be so important for me so I've decided to skip their generation
- at least on Windows 7, you can get an error stating that "api-ms-win-crt-runtime-l1-1-0.dll is missing". You can resolve it by installing Visual C++ Redistributable for Visual Studio described in point 7
- I've tried to install python-ldap instead than ldap3, but I was not able. With "pip install python-ldap" it keeps writing  errors like "error: Microsoft Visual C++ 14.0 is required." but I cannot resolve it whatever I install from Microsoft.
- Macintosh compatibility is needed, I'm trying to do it in a VM but please help if you can.
