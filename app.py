import tkinter as tk
from tkinter import filedialog, Text
from playsound import playsound
from functools import partial
import numpy
import pyaudio
import os

# import sound files and load into unique functions
sounds = []
for filename in os.listdir('key_sounds'):
    if filename != '.DS_Store':
        f = os.path.join('key_sounds', filename)
        if os.path.isfile(f):
            sounds.append(f)


# play note function
def playnote(url):
    playsound(url)


# dict of various note functions (must be initalised as so, cannot pass arguements through button command)
notefuncs = {f'note{i}': partial(
    playnote, url=sounds[i]) for i in range(len(sounds))}

# build gui
root = tk.Tk()
c3 = tk.Button(root, text="c3", command=notefuncs['note0'])
c3.grid()
c3.pack()

root.mainloop()
