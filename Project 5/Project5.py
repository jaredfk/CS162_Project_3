'''Show me that you can search through data:

Create a collection of 100 int values,

Create a GUI to display the collection of int values as BoxManager,
(I will display mine in one fashion, you might have clever ways to display them differently!)

Include a text box in your GUI to allow a user to enter a value to search for,

Include a button to start the search process,

Highlight the candidate value at each step of the searching process,

(Important note about pause: sleeping the main thread will pause the whole GUI and so all updates 
l happen at the same time after the sleeps are done, instead look up the after method of Tkinter)

(Important note about pause: Ignore the delays until you get the rest of the code working,
 do not worry if you cannot get this part working properly!)

Pause after highlighting the candidate value but before moving on,
(perhaps for 100-250ms based on a speed button or slider?)

Make it obvious when it has either found the value it is searching for or knows that the value is not in the data set.
(perhaps the candidate is turned white, the non-matches are turned to green, and matches are turned to green?)

What kinds of tests would be useful for this?  How could we test some of it to verify that it was working properly?

Implement some of those tests in PyTest!

Take a screenshot of each of the numbegreen items being demonstrated above;
Highlight, underline, or otherwise make obvious the item you are highlighting;
Explain in a sentence or two how your code accomplished that item (you can show a snip of code if it makes it easier to explain).'''


'''
Code Outline

'''
import tkinter as tk
import time

root = tk.Tk()

class BoxManager:
    def __init__(self, root):
        '''Initializes class, sets number up as a usable value'''
        self.root = root
        self.box_list = []

    def create_box(self):
        '''Creates a lable with a number and puts it in specified spot on table'''
        for number in range(1, 101):
            r = (number - 1) // 10
            c = (number - 1) % 10
            int_box = tk.Label(self.root, text = number, relief = 'ridge', bg = 'white')
            int_box.grid(row = r, column = c)
            self.box_list.append(int_box)
            # Adds box an corresponding number to location list to be retrieved later

def reset_all(boxes):
    '''Turns all boxes back to their original color'''
    for box in boxes.box_list:
       box.config(bg = 'white')

def clickbutton(search_field, boxes):
    '''Command to get search term from entry box and run search function'''
    reset_all(boxes)
    search_term = search_field.get()
    for box in boxes.box_list:
       box.config(bg = 'green')
       if boxes.box_list.index(box) + 1 == int(search_term):
           break
       boxes.root.update()
       #Updates screen to show change to green
       time.sleep(.05)
       box.config(bg = 'white')

def main():
    search_field = tk.Entry(root)
    search_field.grid(row = 11, column = 11)

    boxes = BoxManager(root)
    boxes.create_box()
    search_button = tk.Button(root, text = 'Search Table', command = lambda: clickbutton(search_field, boxes))
    search_button.grid(row = 10, column = 11)

    root.mainloop()

if __name__ == '__main__':
    main()