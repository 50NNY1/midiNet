import tkinter as tk
from tkinter import filedialog, Text
from functools import partial
from pydub import AudioSegment
from pydub.playback import play
import os

# import sound files and load into unique functions
sounds = []
for i in range(13):
    sounds.append(f'key_sounds/{i+1}.wav')
    print(i)

for i in range(len(sounds)):
    print(sounds[i])


def playnote(url):
    print(url)
    sound = AudioSegment.from_wav(url)
    play(sound)


# dict of various note functions (must be initalised as so, cannot pass arguements through button command)
notefuncs = {f'note{i}': partial(
    playnote, url=sounds[i]) for i in range(len(sounds))}

# build gui
root = tk.Tk()
c3 = tk.Button(root, text="c3", command=notefuncs['note0'])
csharp3 = tk.Button(root, text="c#3", command=notefuncs['note1'])
d3 = tk.Button(root, text="d3", command=notefuncs['note2'])
dsharp3 = tk.Button(root, text="d#3", command=notefuncs['note3'])
e3 = tk.Button(root, text="e3", command=notefuncs['note4'])
f3 = tk.Button(root, text="f3", command=notefuncs['note5'])
fsharp3 = tk.Button(root, text="f#3", command=notefuncs['note6'])
g3 = tk.Button(root, text="g3", command=notefuncs['note7'])
gsharp3 = tk.Button(root, text="g#3", command=notefuncs['note8'])
a3 = tk.Button(root, text="a3", command=notefuncs['note9'])
asharp3 = tk.Button(root, text="a#3", command=notefuncs['note10'])
b3 = tk.Button(root, text="b3", command=notefuncs['note11'])
c4 = tk.Button(root, text="c4", command=notefuncs['note12'])

c3.grid(row=0, column=0)
csharp3.grid(row=0, column=1)
d3.grid(row=0, column=2)
dsharp3.grid(row=0, column=3)
e3.grid(row=0, column=4)
f3.grid(row=0, column=5)
fsharp3.grid(row=0, column=6)
g3.grid(row=0, column=7)
gsharp3.grid(row=0, column=8)
a3.grid(row=0, column=9)
asharp3.grid(row=0, column=10)
b3.grid(row=0, column=11)
c4.grid(row=0, column=12)

root.mainloop()
