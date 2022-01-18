import cv2 as cv

import pyautogui
from PIL import ImageGrab




#Made screenshot of screen & check if mouse should be pressed or not
#depends on position of float on the fishing bar
def fishBarMatching():
    
    while(True):
        #Made a screenshot of Fishing bar in primary screen Albion window must be visible
        fishinBargAreaScreenTaken = ImageGrab.grab(bbox=(838, 537, 1082, 567))
        fishinBargAreaScreenTaken.save('fishingBarArea.png')

        #Load screenshot and picture of for for future comparisons
        fishingAreaMatching = cv.imread('fishingBarArea.png', cv.IMREAD_REDUCED_COLOR_2)
        fishbarUpMatching = cv.imread('fishBarUp.png',cv.IMREAD_REDUCED_COLOR_2)

        #Compare both pictures
        resultMatchingFishbar = cv.matchTemplate(fishingAreaMatching, fishbarUpMatching, cv.TM_CCOEFF_NORMED)
        
        #Declaring variables for location (maxValFishingBar = best result) 
        minValFishingBar, maxValFishingBar, minLocFishingBar, maxLocFishingBar = cv.minMaxLoc(resultMatchingFishbar)
        
        #Checking matching results:
        #if its above 0.7 mouse will be pressed until it will be below 0.7 value then mouse will be relased
        #if value will be below 0.56 (no fishing bar on screenshot) it will break while loop
        if maxValFishingBar >=0.7:
            pyautogui.mouseDown(button='left')
            continue
        elif maxValFishingBar<=0.56:
            break
        else:
            pyautogui.mouseUp(button='left')
            continue
            
#While loop which start functions responsible for full fishing process    
while(True):
    
    fishBarMatching()
    