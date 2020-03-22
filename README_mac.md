## MacOS binaries

The MacOS binaries on https://github.com/nicozanf/web2py-pyinstaller contain Python 3.7.4 (or 2.7.16) 64 bit with all the needed modules and the web2py in the specified version: you don't need anything else to run them on MacOS! After uncompressing the zip file, you just need to click on the web2py icon inside.  

They were produced by me on MacOS Sierra 10.12.6 + security update 2019.001.

## Full MacOS build recipe

1. grab and install the official Python program from https://www.python.org : I've got version 3.7.4 or 2.7.16 (64 bit). If you've chosen python 2, change pip3 with pip, and python3 with python in the following instructions...

2. Open a terminal, update tools with:
"python3 -m pip install --upgrade pip" --> pip-19.2.1
"pip3 install --upgrade setuptools" --> setuptools-41.0.1


3. install PyInstaller with: 
sudo -H pip3 install --upgrade pyinstaller (I've got PyInstaller-3.6 )

4. additional (but not required) packages:  
(only for python 2: install Homebrew from https://brew.sh/#install , then 'brew install unixodbc' )
pip3 install psycopg2-binary = psycopg2-2.7.7
pip3 install pyodbc = pyodbc-4.0.26-cp37-cp37m
pip3 install python-ldap (on the windows message, accept to install the "Command line developer tools"). Rerun:
pip3 install python-ldap

5. grab latest web2py source from https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip (you need at least 2.18.3 for needed changes in gluon\admin.py). Open it to uncompress, in this example on Desktop/web2py


6. take the file build_web2py.py and web2py.mac.spec  from this repository and place it on the Desktop/web2py  folder  

7. edit the file /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PyInstaller/hooks/hook-_tkinter.py and change one of its line according to https://github.com/pyinstaller/pyinstaller/pull/3830  

8. (optional, for having a full working interactive shell) change the fake site.py module included within the PyInstaller installation with the content of the files web2py.site_37.py or web2py.site_27.py from this repository - see comments inside these files for details.
 You will also need to add 'import site' on the top of the file Desktop/web2py/gluon/shell.py 

9. open a terminal, goto Desktop/web2py and run:  

python3 build_web2py.py

10. if everything is fine, you'll obtain web2py_macos.zip on the Desktop/web2py  folder. Inside it, there is the web2py program with both the CMD version and the APP version.  

11. due to a known bug (see https://github.com/pyinstaller/pyinstaller/issues/3820) the APP bundle is not working as it is created. As a simple workaround, you need to create inside it the folder web2py.app/Contents/lib/tcl8/8.5/ and copy there the single file:  

/Library/Frameworks/Python.framework/Versions/3.7/lib/tcl8/8.5/**msgcat-1.6.1.tm**  

## Debugging
The 'normal' binaries have only the external python modules included (i.e. no gluon*). In this way, new versions of web2py can be simply deployed by substituting the web2py source files inside the ZIP file but the main program web2py.py must not be modified.
Sometimes this could be broken due to new requirements. In this case you need to make a 'fat' binary version by changing to True the BUILD_DEBUG variable in build_web2py.py. Then you can examine the new executable (for new modules to be specified in web2py.mac.spec) with the command:  

pyi-archive_viewer web2py.exe  

see https://pyinstaller.readthedocs.io/en/latest/advanced-topics.html#using-pyi-archive-viewer for details


