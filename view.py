import tkinter as tk
from tkinter.font import NORMAL
import tkinter.ttk as ttk
from tkinter import filedialog
import getpass

import controller

global isRunButton, openFilePath, saveDir
isRunButton = False

def open_file_command():
    usrPics = r'\Users\{}\Pictures'.format(getpass.getuser())
    file_path = filedialog.askopenfilename(
        filetypes=[('image file', '*.png;*.jpg;*.jpeg')],
        initialdir=usrPics,
        )
    openFilePath = str(file_path)
    image_choice_label_text.set(openFilePath)

    # UPDATE PATH ENTRY
    # image_choice_entry.configue(state='normal')
    # image_choice_entry.insert(tk.END, file_path)
    # image_choice_entry.configue(state='readonly')

    # if not (image_choice_entry == "" or image_choice_entry == 0):
    #     isRunButton = True

    if not openFilePath == '':
        run_button['state'] = tk.NORMAL
    elif openFilePath == '':
        image_choice_label_text.set('(Required)')

    # if isRunButton == True:
    #     run_button['state'] = tk.NORMAL


def save_directory_command():
    usrPics = r'\Users\{}\Pictures'.format(getpass.getuser())
    dir_path = filedialog.askdirectory(
        initialdir=usrPics,
    )
    saveDir = str(dir_path)

    # UPDATE PATH ENTRY
    # image_savedir_button_entry.configue(state='normal')
    # image_savedir_button_entry.insert(tk.END, saveDir)
    # image_savedir_button_entry.configue(state='readonly')

    image_savedir_label_text.set(saveDir)

def get_saveDir():
    return saveDir

# def get_openFile():
#     return open_file_command.file_path

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
    # ENTRY
    # global image_choice_entry
    # image_choice_entry = tk.Entry(frame, width=40, state='readonly')
    # image_choice_entry.pack()

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
    # ENTRY
    # global image_savedir_button_entry
    # image_savedir_button_entry = tk.Entry(frame, width=40, state='readonly')
    # image_savedir_button_entry.pack()

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
        frame, text="RUN", command=controller.run, state=tk.DISABLED
    )
    run_button.pack()
    

    # if isRunButton == False:
    #     run_button.state(['disabled'])
    # else:
    #     run_button.state(['enabled'])

    root.mainloop()

if __name__ == '__main__':
    view()
