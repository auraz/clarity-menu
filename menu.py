#!/usr/bin/env python3
import rumps

from settings import desktops, reverse_desktops


class ClarityStatusBarApp(rumps.App):

    pass


def attach(desktops):

    for number, description in desktops.items():

        def method(sender, menuitem):
            desktop_number = reverse_desktops[menuitem.title]
            import subprocess
            subprocess.call(['switch_desktop.py', desktop_number])

        setattr(
            ClarityStatusBarApp,
            "custom_method_" + number,
            classmethod(rumps.clicked(description)(method))
        )

if __name__ == "__main__":
    attach(desktops)
    ClarityStatusBarApp("Clarity").run()
