import tkinter as tk 
from tkinter import * 
from functools import partial 
from typing import List 
from pydub import AudioSegment 
from pydub.playback import play
import os
import time
# import sound files and load into unique functions
sounds = []
for i in range(8):
    sounds.append(AudioSegment.from_file(f'drum_sounds/{i+1}.wav'))
for i in range(len(sounds)):
    print(sounds[i])
def playnote(sound):
    play(sound)
#notes array, for labelling buttons
notes = ["c3", "c#3", "d3", "d#3", "e3", "f3",
         "f#3", "g3"]

# dict of various note functions (must be initalised as so, cannot pass arguements through button command)
notefuncs = {f'note{i}': partial(
    playnote, sound=sounds[i]) for i in range(len(sounds))}

#dict to store buttons and button states (on or off)
state = {'buttons': [], 'button_values': [[
    False for i in range(len(sounds))]for i in range(8)]}

#timer functions for sequencing
step = 0
currentstep = []
def step1():
    mixed = AudioSegment 
    temp = None 
    isstep = False
    for j in range(len(sounds)):
        if state['button_values'][0][j] == True:
            isstep = True
            if temp != None:
                mixed = sounds[j].overlay(temp)
            if temp == None:
                mixed = sounds[j]
            temp = sounds[j]
    stepmarker.grid(row=len(sounds)+1,column=0)
    if isstep:
        play(mixed)
def step2():
    mixed = AudioSegment 
    temp = None 
    isstep = False
    for j in range(len(sounds)):
        if state['button_values'][1][j] == True:
            isstep = True
            if temp != None:
                mixed = sounds[j].overlay(temp)
            if temp == None:
                mixed = sounds[j]
            temp = sounds[j]
    stepmarker.grid(row=len(sounds)+1,column=1)
    if isstep:
        play(mixed)
def step3():
    mixed = AudioSegment 
    temp = None 
    isstep = False
    for j in range(len(sounds)):
        if state['button_values'][2][j] == True:
            isstep = True
            if temp != None:
                mixed = sounds[j].overlay(temp)
            if temp == None:
                mixed = sounds[j]
            temp = sounds[j]
    stepmarker.grid(row=len(sounds)+1,column=2)
    if isstep:
        play(mixed)
def step4():
    mixed = AudioSegment 
    temp = None 
    isstep = False
    for j in range(len(sounds)):
        if state['button_values'][3][j] == True:
            isstep = True
            if temp != None:
                mixed = sounds[j].overlay(temp)
            if temp == None:
                mixed = sounds[j]
            temp = sounds[j]
    stepmarker.grid(row=len(sounds)+1,column=3)
    if isstep:
        play(mixed)
def step5():
    mixed = AudioSegment 
    temp = None 
    isstep = False
    for j in range(len(sounds)):
        if state['button_values'][4][j] == True:
            isstep = True
            if temp != None:
                mixed = sounds[j].overlay(temp)
            if temp == None:
                mixed = sounds[j]
            temp = sounds[j]
    stepmarker.grid(row=len(sounds)+1,column=4)
    if isstep:
        play(mixed)
def step6():
    mixed = AudioSegment 
    temp = None 
    isstep = False
    for j in range(len(sounds)):
        if state['button_values'][5][j] == True:
            isstep = True
            if temp != None:
                mixed = sounds[j].overlay(temp)
            if temp == None:
                mixed = sounds[j]
            temp = sounds[j]
    stepmarker.grid(row=len(sounds)+1,column=5)
    if isstep:
        play(mixed)
def step7():
    mixed = AudioSegment 
    temp = None 
    isstep = False
    for j in range(len(sounds)):
        if state['button_values'][6][j] == True:
            isstep = True
            if temp != None:
                mixed = sounds[j].overlay(temp)
            if temp == None:
                mixed = sounds[j]
            temp = sounds[j]
    stepmarker.grid(row=len(sounds)+1,column=6)
    if isstep:
        play(mixed)
def step8():
    mixed = AudioSegment 
    temp = None 
    isstep = False
    for j in range(len(sounds)):
        if state['button_values'][7][j] == True:
            isstep = True
            if temp != None:
                mixed = sounds[j].overlay(temp)
            if temp == None:
                mixed = sounds[j]
            temp = sounds[j]
    stepmarker.grid(row=len(sounds)+1,column=7)
    if isstep:
        play(mixed)

stepfunctions =[step1,step2,step3,step4,step5,step6,step7,step8]
bpmms = 500
def getbpm():
    bpm = int(bpm_box.get())
    bpmms = (60000 / bpm) / 2
    print(bpmms)
def starttimer(first=True):
    global step
    if first:
        play_button['state'] = tk.DISABLED
        play_button.update_idletasks()
        step = 0
    if play_button['state'] == tk.DISABLED:
        step += 1
        if step == 8:
            step = 0
        stepfunctions[step-1]()
        play_button.after(500, starttimer, False)
def stoptimer():
    global step
    play_button['state'] = tk.NORMAL
    step = 0
# build gui
root = tk.Tk()
on = PhotoImage(file="images/on.png")
off = PhotoImage(file="images/off.png")
marker = PhotoImage(file="images/step.png")
#button constructor (without classes, as we are using a dict to manage instances)
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

#create grid of buttons
for i in range(8):
    button_row = []
    for j in range(len(sounds)):
        button = create_button(j, i)
        button.grid(row=j, column=i)
        button_row.append(button)
    state['buttons'].append(button_row)
    
#sequencer parameters
param_col = len(sounds)+1
bpm_button = Button(root, text="BPM Submit", command=getbpm)
bpm_button.grid(row=0, column=param_col)
bpm_box = Entry(root)
bpm_box.grid(row=1, column=param_col)
play_button= Button(root, text="stop/start", command=starttimer)
play_button.grid(row=2, column=param_col)
stop_button= Button(root, text="stop", command=stoptimer)
stop_button.grid(row=3, column=param_col)
stepmarker = Label(image=marker)
stepmarker.grid(row=len(sounds)+1, column=0)
#bit of extra code required for the NN button as it needs to be toggleable
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
nn.grid(row=4, column=param_col)

#render graphics             
root.mainloop()
