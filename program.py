from tkinter import *
from tkinter import font
import urllib.request
from html.parser import HTMLParser
import urllib.error
from tkinter import messagebox


class HTML(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            print("Hyperlink Encountered")
            for attr in attrs:
                print("     Attributes:", attr)
        elif tag == 'p':
            print("Paragraph Tag Encountered")
        elif tag == 'img':
            print("Image Tag Encountered")
            for attr in attrs:
                print("     Attributes:", attr)
        elif tag == 'font':
            print("Font Tag Encountered")
            for attr in attrs:
                print("     Attributes:", attr)
        elif tag == 'h1':
            print("Heading Tag Encountered at Font:1")
        elif tag == 'h2':
            print("Heading Tag Encountered at Font:2")
        elif tag == 'h3':
            print("Heading Tag Encountered at Font:3")
        elif tag == 'h4':
            print("Heading Tag Encountered at Font:4")
        elif tag == 'h5':
            print("Heading Tag Encountered at Font:5")
        elif tag == 'h6':
            print("Heading Tag Encountered at Font:6")
        elif tag == 'b':
            print("Bold Tag Encountered")
        elif tag == 'i':
            print("Italics Tag Encountered")
        elif tag == 'strong':
            print("Important Text Tag Encountered")
        elif tag == 'em':
            print("Emphasized Text Tag Encountered")
        elif tag == 'mark':
            print("Marked Text Tag Encountered")
        elif tag == 'small':
            print("Smaller Text Tag Encountered")
        elif tag == 'del':
            print("Deleted Text Tag Encountered")
        elif tag == 'ins':
            print("Inserted Text Tag Encountered")
        elif tag == 'sub':
            print("Subscript Text Tag Encountered")
        elif tag == 'sup':
            print("Superscript Text Tag Encountered")
        else:
            for attr in attrs:
                if attr == 'bgcolor':
                    print("attr:", attr)

    def handle_data(self, data):
        print("Data:", data)


def search():
    text.delete(1.0, END)
    try:
        with urllib.request.urlopen(entry.get()) as response:
            received_data = response.read()
            text.insert(1.0, received_data)
            rc = str(received_data)
            p.feed(rc)
    except urllib.error.URLError as e:
        messagebox.showerror("Error!", e.reason)
    except urllib.error.HTTPError as e:
        messagebox.showerror("Error!", e.reason)
    except ValueError:
        messagebox.showerror("Error!", "Invalid URL entered.")


def clearTextInput():
    text.delete("1.0", "end")
    entry.delete(0, END)


window = Tk()
window.minsize(500, 400)
window.title('Web Browser')
window.configure(bg="#2F363F")
label = Label(window, text='Enter URL:', bg="#FFFFFF")
entry = Entry(window, width=37, bg="#FFFFFF")
entry.insert(END, "https://www.berkshirehathaway.com/")
p = HTML()
button = Button(window, text='Search', command=search,  bg="#FFFFFF")
button1 = Button(window, text='Clear', command=clearTextInput, bg="#FFFFFF")
button2 = Button(window, text='Exit', command=window.destroy, bg="#FFFFFF")
text = Text(window, bg="#ffffff", fg="#2F363F")

label.grid(row=0, sticky='W', padx=130)
entry.grid(row=0, padx=100)
button.grid(row=1, sticky='W', padx=150)
button1.grid(row=1, sticky='W', padx=270)
button2.grid(row=1, sticky='E', padx=240)
text.grid(row=2)
window.mainloop()