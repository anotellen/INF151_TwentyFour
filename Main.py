# https://programminghistorian.org/en/lessons/creating-and-viewing-html-files-with-python
# write-html-2-mac.py
import webbrowser
import mammoth


def process(path):
    try:
        custom_styles = "b => i"
        result = mammoth.convert_to_html(path, style_map = custom_styles)
        text = result.value
        with open('output.html', 'w') as html_file:
            html_file.write(text)
    except:
        print("Error")

    
    
    
    
def open_html(path):
    filename = path
    try:
        #this is for Jason
        cent_path = "C:/Program Files/CentBrowser/Application/chrome.exe %s"
        webbrowser.get(cent_path).open_new_tab(filename)
    except:
        webbrowser.open_new_tab(filename)
 
