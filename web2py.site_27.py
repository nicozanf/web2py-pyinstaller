"""
web2py.site_27.py

Source:
This is the 3.4 PyInstaller's fake site.py 
(see https://github.com/pyinstaller/pyinstaller/blob/develop/PyInstaller/fake-modules/site.py)
with the addition of the original 2.7 cpython code (see https://github.com/python/cpython/blob/2.7/Lib/site.py )
and adapted for reducing the size of the resulting frozen code

Purpose:
having back additional commands (mainly help and quit) in the python shell

Usage:
after installing PyInstaller, rename this file to site.py and overwrite the existing PyInstaller one;
on Windows 10: C:/Python27/Lib/site-packages/PyInstaller/fake-modules/site.py
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
# The following has been borrowed from https://github.com/python/cpython/blob/2.7/Lib/site.py
# and adapted for reducing the size of the frozen code
#

import os
import sys
import __builtin__

def setquit():
	"""Define new builtins 'quit' and 'exit'.
	These are objects which make the interpreter exit when called.
	The repr of each object contains a hint at how it works.
	"""
	if os.sep == ':':
		eof = 'Cmd-Q'
	elif os.sep == '\\':
		eof = 'Ctrl-Z plus Return'
	else:
		eof = 'Ctrl-D (i.e. EOF)'

	class Quitter(object):
		def __init__(self, name):
			self.name = name
		def __repr__(self):
			return 'Use %s() or %s to exit' % (self.name, eof)
		def __call__(self, code=None):
			# Shells like IDLE catch the SystemExit, but listen when their
			# stdin wrapper is closed.
			try:
				sys.stdin.close()
			except:
				pass
			raise SystemExit(code)
	__builtin__.quit = Quitter('quit')
	__builtin__.exit = Quitter('exit')


class _Printer(object):
    """interactive prompt objects for printing the license text, a list of
    contributors and the copyright notice."""

    MAXLINES = 23

    def __init__(self, name, data, files=(), dirs=()):
        self.__name = name
        self.__data = data
        self.__files = files
        self.__dirs = dirs
        self.__lines = None

    def __setup(self):
        if self.__lines:
            return
        data = None
        for dir in self.__dirs:
            for filename in self.__files:
                filename = os.path.join(dir, filename)
                try:
                    fp = file(filename, "rU")
                    data = fp.read()
                    fp.close()
                    break
                except IOError:
                    pass
            if data:
                break
        if not data:
            data = self.__data
        self.__lines = data.split('\n')
        self.__linecnt = len(self.__lines)

    def __repr__(self):
        self.__setup()
        if len(self.__lines) <= self.MAXLINES:
            return "\n".join(self.__lines)
        else:
            return "Type %s() to see the full %s text" % ((self.__name,)*2)

    def __call__(self):
        self.__setup()
        prompt = 'Hit Return for more, or q (and Return) to quit: '
        lineno = 0
        while 1:
            try:
                for i in range(lineno, lineno + self.MAXLINES):
                    print self.__lines[i]
            except IndexError:
                break
            else:
                lineno += self.MAXLINES
                key = None
                while key is None:
                    key = raw_input(prompt)
                    if key not in ('', 'q'):
                        key = None
                if key == 'q':
                    break

def setcopyright():
    """Set 'copyright' and 'credits' in __builtin__"""
    __builtin__.copyright = _Printer("copyright", sys.copyright)
    __builtin__.credits = _Printer("credits", """\
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.""")
    here = os.path.dirname(os.__file__)
    __builtin__.license = _Printer(
        "license", "See https://www.python.org/psf/license/",
        ["LICENSE.txt", "LICENSE"],
        [os.path.join(here, os.pardir), here, os.curdir])


class _Helper(object):
    """Define the builtin 'help'.
    This is a wrapper around pydoc.help (with a twist).
    """

    def __repr__(self):
        return "Type help() for interactive help, " \
               "or help(object) for help about object."
    def __call__(self, *args, **kwds):
        import pydoc
        return pydoc.help(*args, **kwds)

def sethelper():
    __builtin__.help = _Helper()    

def main():
    """Add standard site-specific directories to the module search path.
    This function is called automatically when this module is imported,
    unless the python interpreter was started with the -S flag.
    """   
    setquit()
    setcopyright()
    sethelper()    


main()  
