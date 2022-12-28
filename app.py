import tkinter as tk
from tkinter import *
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

#notes array, for labelling buttons
notes = ["c3", "c#3", "d3", "d#3", "e3", "f3",
         "f#3", "g3", "g#3", "a3", "a#3", "b3", "c4"]

# dict of various note functions (must be initalised as so, cannot pass arguements through button command)
notefuncs = {f'note{i}': partial(
    playnote, url=sounds[i]) for i in range(len(sounds))}

#dict to store buttons and button states (on or off)
state = {'buttons': [], 'button_values': [
    [False for i in range(8)] for j in range(len(sounds))]}

# build gui
root = tk.Tk()
on = PhotoImage(file="images/on.png")
off = PhotoImage(file="images/off.png")

#button constructor (without classes, as we are using a dict to manage instances)
def create_button(row, col):
    def toggle_button():
        if state['button_values'][col][row]:
            state['buttons'][col][row].config(image=off) 
            state['button_values'][col][row] = False 
        else:
            notefuncs[f'note{row}']()
            state['buttons'][col][row].config(image=on)
            state['button_values'][col][row] = True
    return tk.Button(root, text=notes[row],
                     command=toggle_button, bg='white', 
                     image=off, compound=LEFT, bd=0)

#create grid of buttons
for i in range(8):
    button_row = []
    for j in range(len(sounds)):
        button = create_button(j, i)
        button.grid(row=j, column=i)
        button_row.append(button)
    state['buttons'].append(button_row)
    
#sequencer parameters
#param_col = len(sounds)+1
#bpm_label = Label(root, text="BPM")
#bpm_label.grid(row=0, column=param_col)
#bpm_box = Entry(root)
#bpm_box.grid(row=1, column=param_col)
#play = Button(root, text="play")
#play.grid(row=2, column=param_col)
#stop = Button(root, text="stop")
#stop.grid(row=3, column=param_col)
#
##bit of extra code required for the NN button as it needs to be toggleable
#global nn_state
#nn_state = False
#def nn_toggle():
#    if not nn_state: 
#        nn.config(image=on)
#        nn_state = True
#        #run predict here
#    elif nn_state:
#        nn.config(image=off)
#        nn_state = False
#nn = Button(root, text="neural net", command=nn_toggle, 
#            bg="white", image=off, compound=LEFT, bd=0)
#nn.grid(row=4, column=param_col)

#render graphics             
root.mainloop()
