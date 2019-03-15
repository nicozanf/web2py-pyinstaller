Tested with MacOS Sierra 10.12.6 + security update 2019.001
-----------------------------------------------------------

1. grab and install the official Python program: I've got version 3.7.2,(python-3.7.2-macosx10.9.pkg ) 

2. Open a terminal, update tools with:
"python3 -m pip install --upgrade pip" --> pip-19.0.3
"pip3 install --upgrade setuptools" --> setuptools-40.8.0-py2.py3-none-any.whl


3. install PyInstaller with: 
sudo -H pip3 install pyinstaller (I've got PyInstaller-3.4 )

4. additional (but not required) packages: 
pip3 install psycopg2-binary = psycopg2-2.7.7
pip3 install pyodbc = pyodbc-4.0.26-cp37-cp37m
pip3 install python-ldap (on the windows message, accept to install the "Command line developer tools"). Rerun:
pip3 install python-ldap

5. grab latest web2py source from https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip (you need at least 2.18.3 for needed changes in gluon\admin.py). Open it to uncompress, in this example on Desktop/web2py


6. open terminal, go to Desktop/web2py and run (all in one line):

pyinstaller --clean  --windowed --icon=extras/icons/web2py.icns --hidden-import=gluon.packages.dal.pydal  --hidden-import=gluon.packages.yatl.yatl --hidden-import=site-packages --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl'  web2py.py

7. 
rm dist/web2py
rm __pycache__
rm build
mv dist web2py

8.
copy VERSION, application, extras, gluon, to  Desktop\web2py\web2py.app\Contents\MacOS

9. compress Desktop\web2py and rename the ZIP to web2py_macos.zip

Enjoy!
