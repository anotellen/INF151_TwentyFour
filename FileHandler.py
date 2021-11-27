# https://stackoverflow.com/questions/50123315/how-do-i-create-an-import-file-button-with-tkinter/50135930
# https://pythonguides.com/upload-a-file-in-python-tkinter/

import tkinter as tk
from tkinter import filedialog

def updateDisplay(myString):
    text.set(myString)

def SelectFileAction(event=None):
    filename = filedialog.askopenfilename()
    updateDisplay(filename)

def UploadFileAction():
    print("uploading file: " + filename)

root = tk.Tk()

button = tk.Button(root, text='Choose File', command=SelectFileAction)
button.pack()

text = tk.StringVar()
updateDisplay("No file chosen")
selectedFile = tk.Label(root, textvariable=text)
selectedFile.pack()

button = tk.Button(root, text='Upload', command=UploadFileAction)

root.mainloop()
