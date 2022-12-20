import tkinter as tk
from tkinter import filedialog, Text
from functools import partial
from pydub import AudioSegment
from pydub.playback import play
import os

# import sound files and load into unique functions
urls = []
audiosegments = {}
for i in range(13):
    urls.append(f'key_sounds/{i+1}.wav')
# load audio in before user interaction
for i in range(len(urls)):
    audiosegments["sound{0}".format(i)] = AudioSegment.from_wav(
        urls[i])
playfuncs = {f'play{i}': partial(
    play(audiosegments[f'sound{i}']) for i in range(len(audiosegments)))}

# for i in range(len(audiosegments)):
#     playfuncs["play{0}".format(i)] = play(
#         audiosegments[f'sound{i}'])


notes = ["c3", "c#3", "d3", "d#3", "e3", "f3",
         "f#3", "g3", "g#3", "a3", "a#3", "b3", "c4"]


# dict of various note functions (must be initalised as so, cannot pass arguements through button command)
callnote = {f'note{i}': partial(
    playfuncs[f'play{i}']) for i in range(len(audiosegments))}

# build gui
root = tk.Tk()

for i in range(8):
    for j in range(len(urls)):
        tk.Button(root, text=notes[j], command=callnote[f'note{j}']).grid(
            row=j, column=i)

root.mainloop()
