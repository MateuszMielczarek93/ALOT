import numpy as np
import cv2 as cv
import time
from pynput import mouse
import pyautogui
from PIL import ImageGrab
from pynput.mouse import Controller, Button



while 1>0:
        
        im2 = ImageGrab.grab(bbox=(716, 250, 1050, 440))
        im2.save('fullScreen.png')
        time.sleep(0.1)
          
        fullScreen_img = cv.imread('fullScreen.png',cv.IMREAD_UNCHANGED)
        boy_img = cv.imread('boy.png',cv.IMREAD_UNCHANGED)
        result = cv.matchTemplate(fullScreen_img, boy_img, cv.TM_CCOEFF_NORMED)
        min_val1, max_val1, min_loc1, max_loc1 = cv.minMaxLoc(result)

        match_boy = 0.56
        print(max_val1)
                
        if max_val1 <= match_boy:  
                pyautogui.mouseDown(button='left') 
                pyautogui.mouseUp(button='left')                                                         
                print('click2')
                time.sleep(0.17)
                im2 = ImageGrab.grab(bbox=(716, 250, 1050, 440))
                im2.save('fullScreen.png')
                time.sleep(0.1)
                
                fullScreen_img = cv.imread('fullScreen.png',cv.IMREAD_UNCHANGED)
                boy_img = cv.imread('boy.png',cv.IMREAD_UNCHANGED)
                result = cv.matchTemplate(fullScreen_img, boy_img, cv.TM_CCOEFF_NORMED)
                min_val1, max_val1, min_loc1, max_loc1 = cv.minMaxLoc(result)

        
                while max_val1<=match_boy:
                        im1 = ImageGrab.grab(bbox=(830, 525, 1100, 600))
                        im1.save('fullScreen.jpg')

                        fullScreen_img = cv.imread('fullScreen.jpg',cv.IMREAD_REDUCED_COLOR_4)
                        fishBar_img = cv.imread('fishBar.jpg',cv.IMREAD_REDUCED_COLOR_4)
                        result = cv.matchTemplate(fullScreen_img, fishBar_img, cv.TM_CCOEFF_NORMED)
                        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                        time.sleep(0.1)
                        match = 0.90
                        if max_val >= match:  
                                pyautogui.mouseDown(button='left') 
                                print('click3')
                        else:
                                pyautogui.mouseUp(button='left') 
                                im1 = ImageGrab.grab(bbox=(830, 525, 1100, 600))
                                im1.save('fullScreen.jpg')

                                fullScreen_img = cv.imread('fullScreen.jpg',cv.IMREAD_REDUCED_COLOR_4)
                                fishBar1_img = cv.imread('fishBar1.jpg',cv.IMREAD_REDUCED_COLOR_4)
                                result = cv.matchTemplate(fullScreen_img, fishBar1_img, cv.TM_CCOEFF_NORMED)
                                min_val, max_val3, min_loc, max_loc = cv.minMaxLoc(result)
                                print('click4')
                                if max_val3 <= 0.85:
                                        print(max_val3)
                                        print('click5')      
                                        break
                                        