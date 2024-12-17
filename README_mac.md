## MacOS binaries

The MacOS binaries on https://github.com/nicozanf/web2py-pyinstaller contain Python 3.12.7 with all the needed modules and the web2py in the specified version: you don't need anything else to run them on MacOS! After uncompressing the zip file, you just need to click on the web2py icon inside.

They were produced by me on MacOS 12.7.6.

## Full MacOS build recipe

1. grab and install the official Python program from https://www.python.org : I've got version 3.12.7. 

2. Open a terminal, update tools with:
"python3 -m pip install --upgrade pip" --> pip-24.3.1
"python3 -m pip install --upgrade setuptools" --> setuptools-75.6.0


3. install PyInstaller with: 
sudo -H pip3 install --upgrade pyinstaller (I've got PyInstaller-6.11.1 )

4. additional (but not strictly required) packages:
install Homebrew from https://brew.sh/#install , then 'brew install unixodbc'
pip3 install psycopg2-binary = psycopg2-2.9.10
pip3 install pyodbc = pyodbc-5.2.0
pip3 install python-ldap (on the windows message, accept to install the "Command line developer tools"). Rerun:
pip3 install python-ldap (got python-ldap 3.4.4)

5. goto your Destop folder and run 'git clone --recursive https://github.com/web2py/web2py.git'. In this example it will be installed on your_desktop/web2py - so that you have your_desktop/web2py/web2py.py inside.

6. take the file build_web2py.py and web2py.mac.spec  from this repository and place them on the your_desktop/web2py  folder  

9.goto your_desktop/web2py and run:

python3 build_web2py.py

10. if everything is fine, you'll obtain web2py_macos.zip on the Desktop/web2py  folder. Inside it, there is the web2py program with both the CMD version and the APP version.  

## Debugging
The 'normal' binaries have only the external python modules included (i.e. no gluon*). In this way, new versions of web2py can be simply deployed by substituting the web2py source files inside the ZIP file but the main program web2py.py must not be modified.
Sometimes this could be broken due to new requirements. In this case you need to make a 'fat' binary version by changing to True the BUILD_DEBUG variable in build_web2py.py. Then you can examine the new executable (for new modules to be specified in web2py.mac.spec) with the command:  

pyi-archive_viewer web2py.exe  

see https://pyinstaller.readthedocs.io/en/latest/advanced-topics.html#using-pyi-archive-viewer for details


