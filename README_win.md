## Windows binaries

The windows binaries on https://github.com/nicozanf/web2py-pyinstaller contain Python version 3.12.7 with all the needed modules and the web2py in the specified version. You don't need anything else to run them on Windows.

## Full Windows build recipe

1. get a clean Windows 10 (Windows 10 Professional English build 1809 64 bit, under Virtualbox in my case)
2. grab and install the official Python program: I've got version 3.12.7  (https://www.python.org/ftp/python/3.7.2/python-3.7.3-amd64.exe ) + select  "add Python 3.7 to PATH" during its setup
3. update tools with  
"python -m pip install --upgrade pip"  --> pip-24.3.1  
"pip install --upgrade setuptools" --> setuptools-75.6.0
4. Goto C:\ and grab the latest web2py source with 'git clone --recursive https://github.com/web2py/web2py.git'. In this example it will be installed on C:\web2py - so that you have C:\web2py\web2py.py inside.
5. install PyInstaller with:  
        pip install  --upgrade pyinstaller  (I've got PyInstaller-6.11.1 )  
6. additional (but not strictly required) packages to work better in the Windows world:  
pip install  --upgrade psycopg2 = psycopg2-2.9.10  
pip install  --upgrade pyodbc = pyodbc-5.2.0  
download the file https://github.com/cgohlke/python-ldap-build/releases/download/v3.4.4/python_ldap-3.4.4-cp312-cp312-win_amd64.whl and install it from that folder 
with the command 'pip install python_ldap-3.4.4-cp312-cp312-win_amd64.whl'  

7. copy build_web2py.py, web2py.win.spec and web2py.win_no_console.spec from this repository to C:\web2py\  
8. CD C:\web2py. Run:

    python build_web2py.py

If everything goes fine, you'll obtain the 64 bit binary build zipped as C:\web2py\web2py_win.zip.

## Gothca:

## Debugging
The 'normal' binaries have only the external python modules included (i.e. no gluon*). In this way, new versions of web2py can be simply deployed by substituting the web2py source files inside the ZIP file. But the main program web2py.py must not be modified. 
Sometimes this could be broken due to new requirements; in this case you need to make a 'fat' binary version by changing to True the BUILD_DEBUG variable in build_web2py.py (this works fine only with python 3). Then you can examine the new executable (for new modules to be specified in web2py.win.spec) with the command:  

pyi-archive_viewer web2py.exe  

see https://pyinstaller.readthedocs.io/en/latest/advanced-topics.html#using-pyi-archive-viewer for details


