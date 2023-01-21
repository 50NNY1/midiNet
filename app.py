import tkinter as tk 
from tkinter import * 
from functools import partial 
from typing import List 
import os
import threading
import librosa
import sounddevice as sd
import time

sounds = []
for i in range(8):
    sounds.append(f'drum_sounds/{i+1}.wav')

def playnote(sound):
    arr, samplerate = librosa.load(sound, sr=None, mono=True)
    sd.play(arr,samplerate)
    time.sleep(librosa.get_duration(y=arr,sr=samplerate))
    sd.stop()

notes = ["c3", "c#3", "d3", "d#3", "e3", "f3",
         "f#3", "g3"]

notefuncs = {f'note{i}': partial(
    playnote, sound=sounds[i]) for i in range(len(sounds))}

state = {'buttons': [], 'button_values': [[
    False for i in range(len(sounds))]for i in range(8)]}

step = 0
currentstep = []

def stepfunc():
    global step 
    stepmarker.grid(row=len(sounds)+1,column=step)
    for j in range(len(sounds)):
        if state['button_values'][step][j] == True:
            playnote(sounds[j])
    step+=1
    if step == 8:
        step = 0    

def getbpm():
    bpm = int(bpm_box.get())
    bpmms = (60000 / bpm) / 2
    return int(bpmms)

def starttimer(first=True):
    if first:
        play_button['state'] = tk.DISABLED
        play_button.update_idletasks()
    if play_button['state'] == tk.DISABLED:
        stepfunc()
        play_button.after(getbpm(), starttimer, False)

def stoptimer():
    global step
    play_button['state'] = tk.NORMAL
    step = 0

root = tk.Tk()

#images
on = PhotoImage(file="images/on.png")
off = PhotoImage(file="images/off.png")
marker = PhotoImage(file="images/step.png")

def create_button(row, col):
    def toggle_button():
        if state['button_values'][col][row]:
            state['buttons'][col][row].config(image=off) 
            state['button_values'][col][row] = False 
        else:
            state['buttons'][col][row].config(image=on)
            state['button_values'][col][row] = True
            notefuncs[f'note{row}']()
    return tk.Button(root, text=notes[row],
                     command=toggle_button, bg='white', 
                     image=off, compound=LEFT, bd=0)

for i in range(8):
    button_row = []
    for j in range(len(sounds)):
        button = create_button(j, i)
        button.grid(row=j, column=i)
        button_row.append(button)
    state['buttons'].append(button_row)
    
param_col = len(sounds)+1
bpm_box = Entry(root)
bpm_box.grid(row=0, column=param_col)
play_button= Button(root, text="start", command=starttimer)
play_button.grid(row=1, column=param_col)
stop_button= Button(root, text="stop", command=stoptimer)
stop_button.grid(row=2, column=param_col)
stepmarker = Label(image=marker)
stepmarker.grid(row=len(sounds)+1, column=0)
nn_state = False
def nn_toggle():
    global nn_state
    if(nn_state):
        nn.config(image=off)
        nn_state = False
    elif(not nn_state):
        nn.config(image=on)
        nn_state = True
        #call predict here!
nn = Button(root, text="neural net", command=nn_toggle, 
            bg="white", image=off, compound=LEFT, bd=0)
nn.grid(row=3, column=param_col)

root.mainloop()
