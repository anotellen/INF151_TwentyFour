# https://programminghistorian.org/en/lessons/creating-and-viewing-html-files-with-python
# write-html-2-mac.py
import webbrowser
import mammoth


def process(path):
    
    custom_styles = "b => i"
    result = mammoth.convert_to_html(path, style_map = custom_styles)
    text = result.value
    with open('output.html', 'w') as html_file:
        html_file.write(text)
    
    
    
def open_html():
    #filename = path
    try:
        #this is for Jason
        cent_path = "C:/Program Files/CentBrowser/Application/chrome.exe %s"
        webbrowser.get(cent_path).open_new_tab("output.html")
    except:
        webbrowser.open_new_tab("output.html")
 
