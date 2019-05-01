# A small guide for adding other modules to the binary web2py


According to the web2py manual, if you run web2py **from source** you can import from it any python module that is in the PYTHONPATH (sys.path) - 
which is automatically changed by web2py in order to include also web2py/site-packages (globally) and web2py/application/myapp/modules (inside myapp).  
The last one is preferred if you are planning to distribute the app or you are experimenting with different versions of the same module. 
It also has higher priority and can even be accessed by other apps as web2py/application/anotherapp/modules.

If you run web2py **from the compiled binary**, any system-wide folder will be ignored - only what's down the web2py folder will be normally available. You can check it by yourself with the interactive shell (running `web2py -M -S myapp` inside the web2py's folder) and [the simple helloworld.py module.](https://stackoverflow.com/questions/15746675/how-to-write-a-python-module-package)
 
Modules will be searched in this order: 

1. web2py/application/myapp/modules (inside myapp)
1. web2py/site-packages (globally for all the apps) 
1. web2py
1. web2py/gluon/packages/yatl
1. web2py/gluon/packages/dal
1. web2py/base_library.zip (contains base libraries from python)

Also, you have modules inside the web2py binary made by PyInstaller. You can look inside this compressed file with the pyi-archive_viewer utility of PyInstaller.

## Differences and Troubleshooting

What's different and problematic in the 'running from binary' mode is that it's not so easy to install modules inside them. You have the following options:

- **manual copy**: you can pip-install them on a full system (that has python of the same version of the binary one) and manually copy 
the related files inside the binary folders. For complex module, you also have to copy all the files for the 
related pre-requisites - and possibly test them one by one. 
- **pip install**: on a full system (that has python of the same version of the binary one) you can open a shell and go to the web2py folder. Here, you can issue the command `pip install -t site-packages <package_name>` or even `pip install -t applications/myapp/modules <package_name>`. This works fine for simple modules like numpy ;-) - thank 
rāma <ranjeev.hs@gmail.com> for this suggestion!


Unfortunately, this could fail; expecially if the modules contains binary files. 
In this case, the last resort is to try to compile the binary version by yourself  from a working web2py source - following the instructions on my repository and specifying your additional needed modules. Maybe PyInstaller will play the module dependency game better than you ;-)
