# https://stackoverflow.com/questions/50123315/how-do-i-create-an-import-file-button-with-tkinter/50135930
# https://pythonguides.com/upload-a-file-in-python-tkinter/

import tkinter as tk
from tkinter import filedialog
from Main import process
from Main import open_html

filename = ""

def updateDisplay(myString):
    text.set(myString)

def SelectFileAction(event=None):
    global filename
    filename = filedialog.askopenfilename()
    updateDisplay(filename)

def processCallback():
    try:
        global filename
        process(filename)
        updateDisplay("Filetype {} converted successfully!".format(filename.split(".")[1]))
    except:
        updateDisplay("Failed to convert file: check filetype and encoding!")
        
# Opens pdf files but downloads doc files
def open_file():
    try:    
        open_html()
    except:
        updateDisplay("File not found: make sure you proccessed your file first!")
        

root = tk.Tk()
root.title('Canvas Content Automation Tool')
root.geometry("400x200")

button = tk.Button(root, text='Choose File', command=SelectFileAction)
button2 = tk.Button(root, text='Process', command=processCallback)
button3 = tk.Button(root, text='Open File', command=open_file)

button.pack()
button2.pack()
button3.pack()

text = tk.StringVar()
updateDisplay("No file chosen")

'''
button = tk.Button(root, text='Upload', command=UploadFileAction)

'''

selectedFile = tk.Label(root, textvariable=text)
selectedFile.pack()
root.mainloop()
