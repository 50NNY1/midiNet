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

root = tk.Tk()
root.mainloop()
playsound(sounds[0])
playsound(sounds[3])
playsound(sounds[7])
