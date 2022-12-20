import tkinter as tk
from tkinter import filedialog, Text
from functools import partial
from typing import List
from pydub import AudioSegment
from pydub.playback import play
import os

# import sound files and load into unique functions
sounds = []
for i in range(13):
    sounds.append(f'key_sounds/{i+1}.wav')


def playnote(url):
    sound = AudioSegment.from_wav(url)
    play(sound)


notes = ["c3", "c#3", "d3", "d#3", "e3", "f3",
         "f#3", "g3", "g#3", "a3", "a#3", "b3", "c4"]


# dict of various note functions (must be initalised as so, cannot pass arguements through button command)
notefuncs = {f'note{i}': partial(
    playnote, url=sounds[i]) for i in range(len(sounds))}

# build gui
root = tk.Tk()


state = {'buttons': [], 'button_values': [
    [False for i in range(8)] for j in range(len(sounds))]}


def create_button(row, col):
    def toggle_button():
        state['button_values'][row][col] = not state['button_values'][row][col]
        if state['button_values'][row][col]:
            state['buttons'][row][col].config(bg='green')
        else:
            state['buttons'][row][col].config(bg='red')
        notefuncs[f'note{row}']()
    return tk.Button(root, text=notes[row],
                     command=toggle_button, bg='white')


for i in range(8):
    button_row = []
    for j in range(len(sounds)):
        button = create_button(j, i)
        button.grid(row=j, column=i)
        button_row.append(button)
    state['buttons'].append(button_row)
    # buttons.append(tk.Button(root, text=notes[j], command=notefuncs[f'note{j}']).grid(
    #     row=j, column=i))


root.mainloop()
