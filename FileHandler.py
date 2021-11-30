# https://stackoverflow.com/questions/50123315/how-do-i-create-an-import-file-button-with-tkinter/50135930
# https://pythonguides.com/upload-a-file-in-python-tkinter/

import tkinter as tk
from tkinter import filedialog
from Main import process

filename = "INF151_Syllabus.docx"

def updateDisplay(myString):
    text.set(myString)

def SelectFileAction(event=None):
    global filename
    filename = filedialog.askopenfilename()
    updateDisplay(filename)

def processCallback():
    global filename
    process(filename)


root = tk.Tk()

button = tk.Button(root, text='Choose File', command=SelectFileAction)
button2 = tk.Button(root, text='Process', command=processCallback)

button.pack()
button2.pack()

text = tk.StringVar()
updateDisplay("No file chosen")

'''
button = tk.Button(root, text='Upload', command=UploadFileAction)

'''

selectedFile = tk.Label(root, textvariable=text)
selectedFile.pack()
root.mainloop()
