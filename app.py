import tkinter as tk
import numpy as np
from tkinter import *
from functools import partial
from typing import List
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import os
import librosa
import sounddevice as sd
import time

sounds = []
for i in range(8):
    url = (f'drum_sounds/{i+1}.wav')
    arr, samplerate = librosa.load(url, sr=None, mono=True)
    sounds.append({'arr': arr, 'samplerate': samplerate})


def playnote(arr, samplerate):
    sd.play(arr, samplerate)
    # time.sleep(librosa.get_duration(y=arr, sr=samplerate))
    # sd.wait()


notes = ["c3", "c#3", "d3", "d#3", "e3", "f3",
         "f#3", "g3"]

notefuncs = {f'note{i}': partial(
    playnote, arr=sounds[i]['arr'],
    samplerate=sounds[i]['samplerate']) for i in range(len(sounds))}

state = {'buttons': [], 'button_values': [[
    False for i in range(len(sounds))]for i in range(8)]}

step = 0
currentstep = []

# short term fourier transforms dictionary for audio overlay
stft_data = {i: librosa.core.stft(audio) for i, audio in enumerate(
    [obj['arr']for obj in sounds])}

model = load_model('model.h5')


def stepfunc():
    global step
    stepmarker.grid(row=len(sounds)+1, column=step)
    stepindexes = [i for i, x in enumerate(state['button_values'][step]) if x]
    if len(stepindexes) > 0:
        combinedaudio = stft_data[stepindexes[0]]
        for i in range(1, len(stepindexes)):
            stft_padded = librosa.util.fix_length(stft_data[stepindexes[i]],
                                                  size=combinedaudio.shape[1])
            combinedaudio = combinedaudio + stft_padded
        overlayedaudio = librosa.core.istft(combinedaudio)
        sd.play(overlayedaudio, sounds[0]['samplerate'])
        # sd.wait()
    step += 1
    if step == 8:
        if nn_state:
            curseq = np.array(state['button_values']).astype(float)
            pred = model.predict(curseq.reshape(1, 8, 8))
            print(pred[0].astype(bool))
            state['button_values'] = pred[0].astype(bool)
            for i in range(8):
                for j in range(len(sounds)):
                    if pred[0][i][j].astype == True:
                        state['buttons'][i][j].config(image=off)
                    else:
                        state['buttons'][i][j].config(image=on)
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

# images
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
play_button = Button(root, text="start", command=starttimer)
play_button.grid(row=1, column=param_col)
stop_button = Button(root, text="stop", command=stoptimer)
stop_button.grid(row=2, column=param_col)
stepmarker = Label(image=marker)
stepmarker.grid(row=len(sounds)+1, column=0)
nn_state = False


def nn_toggle():
    global nn_state
    if (nn_state):
        nn.config(image=off)
        nn_state = False
    elif (not nn_state):
        nn.config(image=on)
        nn_state = True


nn = Button(root, text="neural net", command=nn_toggle,
            bg="white", image=off, compound=LEFT, bd=0)
nn.grid(row=3, column=param_col)

root.mainloop()
