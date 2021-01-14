# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:48:58 2021

@author: rpic84
"""

# -*- coding: utf-8 -*-
### SETTING YOUR WORKING DIRECTORY
import os
os.chdir('your_working_directory_path')

### IMPORTING PACKAGES
import pyautogui 
import keyboard
import win32api,win32con
import time

### GLOBAL VARIABLES
delay=0.1
x_pos,y_pos=1550,970

def double_click(x,y,delay):
    """
    Defining a function that double clicks at a given position (x,y) and leaving a delay between the two clicks.

    Parameters
    ----------
    x : int
        x position of the point to click.
    y : int
        y position of the point to click.
    delay : float
        delay in seconds between the two clicks.

    Returns
    -------
    None.

    """
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

for i in list(range(3)[::-1]): # countdown to let 3s to select the right window
    print(i+1)
    time.sleep(1)

while not(keyboard.is_pressed('q')): # you can press q to leave the loop at any time
    while not(keyboard.is_pressed('q')):
        if pyautogui.locateOnScreen('try_code.png',confidence=0.8)!=None: #if it encounters a question that need a text answer
            # reloading the page and waiting before launching the next questions
            pyautogui.press('F5')
            time.sleep(2)
            double_click(x_pos,y_pos,delay)
        else:
            # pressing the keys to answers
            pyautogui.keyDown('2')
            pyautogui.keyDown('1')
            if pyautogui.locateOnScreen('try_code.png',confidence=0.8)==None: #if it is not a question that need a text answer
                double_click(x_pos,y_pos,delay) 
            time.sleep(delay)


