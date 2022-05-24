import tkinter as tk
from tkinter.font import NORMAL
import tkinter.ttk as ttk
from tkinter import filedialog
import getpass

import numpy as np
from numpy import save

# import controller

global isRunButton, openFilePath, saveDir
isRunButton = False

def open_file_command():
    usrPics = r'\Users\{}\Pictures'.format(getpass.getuser())
    global file_path
    file_path = filedialog.askopenfilename(
        filetypes=[('image file', '*.png;*.jpg;*.jpeg')],
        initialdir=usrPics,
        )
    openFilePath = str(file_path)
    image_choice_label_text.set(openFilePath)

    if not openFilePath == '':
        run_button['state'] = tk.NORMAL
        image_savedir_label_text.set('C:/Users/{}/Pictures'.format(getpass.getuser()))
    elif openFilePath == '':
        image_choice_label_text.set('(Required)')


def save_directory_command():
    usrPics = r'\Users\{}\Pictures'.format(getpass.getuser())
    dir_path = filedialog.askdirectory(
        initialdir=usrPics,
    )
    saveDir = str(dir_path)
    if saveDir == '' or saveDir == 'PY_VAR1':
        saveDir = str(usrPics)

    image_savedir_label_text.set(saveDir)

def get_saveDir():
    return saveDir

# def get_openFile():
#     return openFilePath

def set_processTime(time):
    processTime.set(time)

def view():
    root = tk.Tk()
    root.geometry('400x175')
    root.title('genshin bot')

    frame = ttk.Frame(root)
    frame.pack(fill = tk.BOTH, padx=20, pady=10)

    # IMAGE CHOISE
    image_choice_button = tk.Button(
        frame,
        text='OPEN FILE',
        command=open_file_command,
        width=20,
        height=1,
        )
    image_choice_button.pack()

    global image_choice_label_text
    image_choice_label_text = tk.StringVar(value='(Required)')
    image_choice_label = tk.Label(frame, textvariable=image_choice_label_text)
    image_choice_label.pack()



    # SAVE DIR CHOICE
    image_savedir_button = tk.Button(
        frame,
        text="SAVE AS",
        command=save_directory_command,
        width=20,
        height=1,
        )
    image_savedir_button.pack()

    global image_savedir_label_text
    image_savedir_label_text = tk.StringVar(value="")
    image_savedir_label = tk.Label(frame, textvariable=image_savedir_label_text)
    image_savedir_label.pack()


    # PROCESS TIME
    global processTime
    processTime = tk.StringVar(value="")
    processTimeEntry = tk.Label(frame, textvariable=processTime)
    processTimeEntry.pack()


    # RUN
    global run_button
    run_button = tk.Button(
        frame, text="RUN", command=run, state=tk.DISABLED
    )
    run_button.pack()

    root.mainloop()



import cv2
import time
def run():
    startTime = time.time()


    before_file = file_path
    # savePath = saveDir + ('/Genshin.png')
    savePath = image_savedir_label_text.get()
    print('before_file is',before_file,
    'savePath is', savePath)

    img1 = cv2.imread(str(before_file))
    print(img1.shape)
    img_genshin = cv2.imread('./pic/genshin.png')

    # GET IMAGE RESOLUTION
    height, width = img1.shape[:2]
    genHeight, genWidth = img_genshin.shape[:2]
    resize_img_genshin = cv2.resize(img_genshin, dsize=None, fx=width/7, fy=width/7)

    # IMAGE PLACE
    img1[:height,:width] = resize_img_genshin

    # OUTPUT
    cv2.imwrite(savePath, resize_img_genshin)


    endTime = time.time()
    endTime = endTime - startTime
    set_processTime()

if __name__ == '__main__':
    view()
