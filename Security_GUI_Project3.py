#Jared Knowlton

# Project 3, Basic GUI

import tkinter

root = tkinter.Tk()
# Password game
class NumPad:
    '''First funciton: password code'''
    def __init__(self, number):
        self.number = number # 1 - 9

    def create_button(self, number, r, c):
        '''Assembles GUI from tkinter library''' 
        button = tkinter.Button(root, text = number)
        button.grid(row = r, column =c)

def main():
    my_label = tkinter.Label(root, text = 'Enter Passcode')
    entry_line = tkinter.Entry(root)
    my_label.grid(row = 0, column = 2)
    entry_line.grid(row = 1, column = 2)
    
    r = 2
    c = 0
    for i in range(10):
        num_button = NumPad(i)
        if i == 3:
            r += 1
            c = 1
            num_button.create_button(i, r, c)
        elif i == 6:
            r += 1
            c = 1
            num_button.create_button(i, r, c)
        elif i == 9:
            r += 1
            c = 2
            num_button.create_button(i, r, c)
        else:
            c +=1
            num_button.create_button(i, r, c)
            

                



main()
root.mainloop()
'''Ask for input from user'''
# Check to see if its correct password
# If correct access granted
# Ask again if not correct X 3
# After 3 times execute next function


'''Function 2: sercurity questions'''
# Asks for security question answers
