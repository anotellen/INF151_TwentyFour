# CITATIONS ----------
# Code to write to HTML in Python written by William J. Turkel and Adam Crymble: 
# https://programminghistorian.org/en/lessons/creating-and-viewing-html-files-with-python

import webbrowser
import mammoth
import Setup
from html.parser import HTMLParser

parser = HTMLParser()
f = open('outputHTML.html','w')

with open("INF151_Syllabus.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    text = result.value
    #print(text)
    with open('outputHTML.html', 'w') as html_file:
        f.write(text)

f.close()

#Change path to reflect file location
filename = Setup.filePath + 'outputHTML.html'
webbrowser.open_new_tab(filename)
