'''Create another program (yes you can start with your old code!) to now include 9 more text
boxes (all 10 held within some kind of collection, such as a list) and change the listener
to find the smallest number from the textboxes and display it in the label

Now that that is working, let’s change the button one more time; have the button,
when clicked, change the label's text to match that of the next smaller number in the list
of textboxes.
(so if you had the numbers 1, 5, 3, 7, 8, 3, 6, 9, 0, 12 in the text boxes, then the first
click would display a 0, the second click would display a 1, the next a 3, the next a 3
(since there is another 3 in the list), and so on)

Create a few PyTests similar to before.'''

import tkinter as tk

root = tk.Tk()
root.title('Number Search')


class TextBox:
    def __init__(self, number):
        self.number = number
    
    def create_textbox(self, number):
        txtbox = tk.Label(root, text = number, activebackground = 'yellow', state = 'DISABLED')
        txtbox.pack()


def clickbutton():
    '''Copies the text in the entry line into the label'''
    min_num = min(textbox_list)    
    label1.configure(text = min_num)
    textbox_list.remove(min_num)
    
label1 = tk.Label(root, text = 'Press the button to cycle through the above list in acending order')
textbox_list = [4, 2 ,17, 9, 1, 6, 8, 4, 3, 10]

for i in textbox_list:
    textbox = TextBox(i)
    textbox.create_textbox(i)


button1 = tk.Button(root, text = 'Show next lowest number', command = clickbutton)

button1.pack()
label1.pack()

root.mainloop()