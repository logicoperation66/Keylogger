import pynput

from pynput.keyboard import Key, Listener

def press(key):
    print(f"f{key} wciśniety")

def release(key):
    print(f"{key} zawolniony")

with Listener(on_press=press, on_release=release) as a listener:
    listener.join()