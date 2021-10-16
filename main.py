import pynput

from pynput.keyboard import Key, Listener

def press(key):
    print(f"{key} wciśniety")

def release(key):
    if key == Key.esc:
        return False

with Listener(on_press=press, on_release=release) as listener:
    listener.join()
