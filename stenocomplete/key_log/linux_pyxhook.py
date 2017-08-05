from Xlib import XK

from key_log import pyxhook


class Logger:
    def __init__(self, completer):
        self.completer = completer

    def run(self):
        hook_manager = pyxhook.HookManager()
        hook_manager.KeyDown = self.OnKeyPress
        hook_manager.HookKeyboard()
        hook_manager.start()

    def OnKeyPress(self, event):
        if event.Key == "space":
            self.completer.complete_whitespace()
        elif event.Key == "BackSpace":
            self.completer.complete_backspace()
        else:
            try:
                key_number = getattr(XK, "XK_" + event.Key)
                key = XK.keysym_to_string(key_number)
                if key is not None:
                    self.completer.complete_letter(key)
            except AttributeError:
                pass
