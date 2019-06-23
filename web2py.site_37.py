"""
web2py.site_37.py

Source:
This is the 3.4 PyInstaller's fake site.py 
(see https://github.com/pyinstaller/pyinstaller/blob/develop/PyInstaller/fake-modules/site.py)
with the addition of the original 3.7 cpython code (see https://github.com/python/cpython/blob/3.7/Lib/site.py )
and adapted for reducing the size of the resulting frozen code

Purpose:
having back additional commands (mainly help and quit) in the python shell

Usage:
after installing PyInstaller, rename this file to site.py and overwrite the existing PyInstaller one;
on Windows 10: C:/users/my_name/AppData/Local/Programs/Python/Python37/Lib/site-packages/PyInstaller/fake-modules/site.py
on Mac: /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PyInstaller/fake-modules/site.py

"""



#-----------------------------------------------------------------------------
# Copyright (c) 2013-2018, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


"""
This is a fake 'site' module available in default Python Library.

The real 'site' does some magic to find paths to other possible
Python modules. We do not want this behaviour for frozen applications.

Fake 'site' makes PyInstaller to work with distutils and to work inside
virtualenv environment.
"""

# Marker to be used in our test-suite.
__pyinstaller__faked__site__module__ = True

# TODO test the following code stub from real 'site' module.


# Prefixes for site-packages; add additional prefixes like /usr/local here
PREFIXES = []

# Enable per user site-packages directory
# set it to False to disable the feature or True to force the feature
ENABLE_USER_SITE = False


# For distutils.commands.install
# These values are initialized by the getuserbase() and getusersitepackages()
# functions, through the main() function when Python starts.
# Issue #1699: Freezing pip requires 'site.USER_SITE' to be a 'str' not None.
USER_SITE = ''
USER_BASE = None


#
# The following has been borrowed from https://github.com/python/cpython/blob/3.7/Lib/site.py
# and adapted for reducing the size of the frozen code
#

import os
import sys
import builtins
import _sitebuiltins


def setquit():
    """Define new builtins 'quit' and 'exit'.
    These are objects which make the interpreter exit when called.
    The repr of each object contains a hint at how it works.
    """
    if os.sep == '\\':
        eof = 'Ctrl-Z plus Return'
    else:
        eof = 'Ctrl-D (i.e. EOF)'

    builtins.quit = _sitebuiltins.Quitter('quit', eof)
    builtins.exit = _sitebuiltins.Quitter('exit', eof)


def setcopyright():
    """Set 'copyright' and 'credits' in builtins"""
    builtins.copyright = _sitebuiltins._Printer("copyright", sys.copyright)
    if sys.platform[:4] == 'java':
        builtins.credits = _sitebuiltins._Printer(
            "credits",
            "Jython is maintained by the Jython developers (www.jython.org).")
    else:
        builtins.credits = _sitebuiltins._Printer("credits", """\
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.""")
    files, dirs = [], []
    builtins.license = _sitebuiltins._Printer(
        "license",
        "See https://www.python.org/psf/license/",
        files, dirs)


def sethelper():
    builtins.help = _sitebuiltins._Helper()

def main():
    """Add standard site-specific directories to the module search path.
    This function is called automatically when this module is imported,
    unless the python interpreter was started with the -S flag.
    """   
    setquit()
    setcopyright()
    sethelper()    


main()  
    