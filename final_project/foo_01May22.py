#!/usr/bin/env python3

#
# foo.py - some randome ideas. 
# 01May22   Richard Yang, 
#


def print_space():
    global counter
    string = ['=']*80 + ['\n']
    string = string*22
    string = ''.join(string) 
    print()
    print(string)
    counter += 1
    time.sleep(nap)

def print_pos(p):
    global counter
    global pos
    if p == 'd':
        pos += 1
    elif p == 'a':
        pos -= 1

    else:
        pass

    if pos < 0:
        pos = 0
    elif pos > 79:
        pos = 79
    string = ['=']*80 + ['\n']
    string = string*15
    string = string + ['=']*(pos)+['_']+['=']*(80-pos-1) +['\n']

    string = string + (['=']*80 + ['\n'])*6

    string = ''.join(string) 
    print()
    print(string)
    counter += 1
    time.sleep(nap)


def print_pos_arr(p):
    global X
    global Y
    global counter
    global pos
    if p == 'd':
        pos += 1
    elif p == 'a':
        pos -= 1

    else:
        pass

    if pos < 0:
        pos = 0
    elif pos > 79:
        pos = 79

    #coord = np.zeros((X,Y))    # use two arrays, one number and one text
                                # the number type represents position coord
                                # the text of the same shape is the display
    string = ['=']*80 + ['\n']
    string = string*15
    string = string + ['=']*(pos)+['_']+['=']*(80-pos-1) +['\n']

    string = string + (['=']*80 + ['\n'])*6

    string = ''.join(string) 
    print()
    print(string)
    counter += 1
    time.sleep(nap)


import time
import keyboard
import numpy as np

counter = 0
pos = 1
nap = 0.1
X = 80
Y = 22







while True:
    try:
        if keyboard.is_pressed('q'):
            print('Exited out')
            break
        elif keyboard.is_pressed('d'):
            print()
            print('some action')
            print_pos('d')
            print('counter = %d' %counter)
        elif keyboard.is_pressed('a'):
            print()
            print('some action')
            print_pos('a')
            print('counter = %d' %counter)
            
            

        else:
            #print_space()
            print_pos('')
            print('counter = %d' %counter)
    except:
        print('something else')
        break
