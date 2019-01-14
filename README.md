# clarity-menu
Statusbar Menu for clarity-code for OS X

Menu provides UI to quickly switch desktops for http://www.shirt-ediss.me/clarity/

# installation

mkvirtualenv clarity-code --python=python3

pip install rumps

# configuration

Edit settings.py to be similar with output of `sw` command.

chmod +x menu.py

# run

Development:

./menu.py

Everyday use:

Create sh file somewhere, name it clarity.sh
```
#! /bin/bash
~/.virtualenvs/clarity-menu/bin/python ~/repos/desktops/clarity-menu/menu.py &
```
chmod +x clarity.sh

Add this file to login items in OS X settings.



# notes

Not working when complied with py2app for unknown reason.
