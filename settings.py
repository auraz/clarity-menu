#!/usr/bin/env python3


# list of desktops and shortcut/description per desktop
# output of `sw` command with descktops more readable names.
# names should be unique,
desktops = {
    '0': "Empty Desktop",
    '1': "Start desktop",
    '2': "Composing",
    '3': "Software architecture",
    '4': "Art",
    '5': "Writing",
    '6': "Make travel memories"
}


reverse_desktops = {v:k for k,v in desktops.items()}
