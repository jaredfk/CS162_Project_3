'''Prototype a GUI with a button, a text box, and a label,

Show how event listeners work by having a button that when pressed will copy the text 
from the text box and place it on the label.

Is there any way to automate some tests on these graphical objects?
(Of course there is! But let’s stay simple for the moment)

Create a few PyTests that will work with the data behind the scenes
(maybe a test that checks the default value in your text box, label, 
or that some variables has an expected value)'''

import tkinter as tk

root = tk.Tk()

def clickbutton():
    '''Copies the text in the entry line into the label'''
    label1.configure(text = your_entry.get())

label1 = tk.Label(root, text = 'Your text will be copied here')
your_entry = tk.StringVar()
txtbox = tk.Entry(root, textvariable = your_entry)

button1 = tk.Button(root, text = 'Copy text', command = clickbutton)

button1.pack()
txtbox.pack()
label1.pack()

root.mainloop()