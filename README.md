# clarity-menu
Statusbar Menu for clarity-code for OS X

Menu provides UI to quickly switch desktops for http://www.shirt-ediss.me/clarity/

![](/images/demo.png?raw=true "Demo")

# installation

mkvirtualenv clarity-code --python=python3

pip install rumps

# configuration

Edit settings.py to be similar with output of `sw` command. Look at the settings.py for example.

chmod +x menu.py

# run

Development:

./menu.py

Everyday use: 
(Note: this is workaround, as py2app does not work for some reason.)

1) Create sh file somewhere, name it clarity.sh
```
#! /bin/bash
~/.virtualenvs/clarity-menu/bin/python ~/repos/desktops/clarity-menu/menu.py &
```
chmod +x clarity.sh

2) In automator create application, with single entry: Run AppleScript. 
(Note: Change iTerm to Terminal, if you don't have iTerm)
```
on run {input, parameters}
	tell application "iTerm"
		set newWindow to (create window with default profile)
		tell current session of newWindow
			write text "/Users/kry/bin/clarity.sh"
		end tell
		delay 1
		quit
	end tell
	return input
end run
```
3) Add automator app from step 2 to login items in OS X settings.


# screenshot



# notes

Not working when complied with py2app for unknown reason.
