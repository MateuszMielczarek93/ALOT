import cv2 as cv
import time
import pyautogui
from PIL import ImageGrab


def floatMatching():
    time.sleep(2)
    while(True):
        
        fishingAreaScreenTaken = ImageGrab.grab(bbox=(770, 310, 932, 414))
        fishingAreaScreenTaken.save('fishingArea.png')
        
        fishingAreaMatching = cv.imread('fishingArea.png', cv.IMREAD_REDUCED_COLOR_2)
        floatMatching = cv.imread('float.png',cv.IMREAD_REDUCED_COLOR_2)
        
        resultMatching = cv.matchTemplate(fishingAreaMatching, floatMatching, cv.TM_CCOEFF_NORMED)
        
        minValFishing, maxValFishing, minLocFishing, maxLocFishing = cv.minMaxLoc(resultMatching)
        
        if maxValFishing <=0.65:
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
                fishBarMatching()
                break
        else:
            continue
def fishBarMatching():
    
    while(True):
        fishinBargAreaScreenTaken = ImageGrab.grab(bbox=(838, 537, 1082, 567))
        fishinBargAreaScreenTaken.save('fishingBarArea.png')

        fishingAreaMatching = cv.imread('fishingBarArea.png', cv.IMREAD_REDUCED_COLOR_2)
        fishbarUpMatching = cv.imread('fishBarUp.png',cv.IMREAD_REDUCED_COLOR_2)

        resultMatchingFishbar = cv.matchTemplate(fishingAreaMatching, fishbarUpMatching, cv.TM_CCOEFF_NORMED)
        
        minValFishingBar, maxValFishingBar, minLocFishingBar, maxLocFishingBar = cv.minMaxLoc(resultMatchingFishbar)
        
        if maxValFishingBar >=0.7:
            pyautogui.mouseDown(button='left')
            continue
        elif maxValFishingBar<=0.56:
            break
        else:
            pyautogui.mouseUp(button='left')
            continue 

while (True):
    time.sleep(1)
    pyautogui.mouseUp(button='left')
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
    time.sleep(1)
    floatMatching()

   
