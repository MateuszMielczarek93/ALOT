import numpy as np
import cv2 as cv
import time
from pynput import mouse
import pyautogui
from PIL import ImageGrab
from pynput.mouse import Controller, Button
import tkinter #gui tbd
import win32gui

#Made screenshot of screen & check if boy was founded on saved screen, if yes pull up boy
def boyMatching():
    
    fishingAreaScreenTaken = ImageGrab.grab(bbox=(600, 150, 1300, 700))
    fishingAreaScreenTaken.save('fishingArea.png')

    fishingAreaMatching = cv.imread('fishingArea.png', cv.IMREAD_REDUCED_COLOR_2)
    boyMatching = cv.imread('boy.png',cv.IMREAD_REDUCED_COLOR_2)

    resultMatching = cv.matchTemplate(fishingAreaMatching, boyMatching, cv.TM_CCOEFF_NORMED)
    
    min_val1, max_val1, min_loc1, max_loc1 = cv.minMaxLoc(resultMatching)
    
    print(max_val1)
    
    #time.sleep(0.15)
    

    if max_val1 <=0.69:
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')
            print('if w matchu')
    
    












while True:
    print('whilestart')
    boyMatching()
    print('while')
    
    

'''
if cv.waitKey(1) == ord('q'):
    break
'''