import tkinter as tk
from tkinter import filedialog, Text
import os
import numpy
import pyaudio
root = tk.Tk()
root.mainloop()
pa = pyaudio.PyAudio()

pa = pyaudio.PyAudio()
strm = pa.open(
    format=pyaudio.paInt16,
    channels=2,
    rate=44100,
    output=True,
)
s = []

sounds = {}
for filename in os.listdir('key sounds')(13):
    f = os.path.join('key sounds', filename)
    if os.path.isfile(f):
        print(f)
