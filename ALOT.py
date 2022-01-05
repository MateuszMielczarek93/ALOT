import cv2 as cv
import time
import pyautogui
from PIL import ImageGrab
import tkinter #gui to be done


#Made screenshot of screen & check if float was founded on saved screen,
#if not then left mouse button will be pressed to pull out float
def floatMatching():
    
    #sleep function becouse game need time to throw float
    time.sleep(2)
    while(True):
    
        #Made a screenshot of primary screen Albion window must be visible
        fishingAreaScreenTaken = ImageGrab.grab(bbox=(600, 220, 1250, 500))
        fishingAreaScreenTaken.save('fishingArea.png')
        
        #Load screenshot and picture of float for comparisons
        fishingAreaMatching = cv.imread('fishingArea.png', cv.IMREAD_REDUCED_COLOR_2)
        floatMatching = cv.imread('float.png',cv.IMREAD_REDUCED_COLOR_2)
        
        #Compare both pictures
        resultMatching = cv.matchTemplate(fishingAreaMatching, floatMatching, cv.TM_CCOEFF_NORMED)
        
        #Declaring variables for location (maxValFishing = best result)
        minValFishing, maxValFishing, minLocFishing, maxLocFishing = cv.minMaxLoc(resultMatching)
        
        #Checking maximum result of matching, if its below 0.60 (flot go underwater)
        #Press mouse for catch a fish
        
        if maxValFishing <=0.65:
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
                #Starting function for play fishbar minigame
                fishBarMatching()
                break
        else:
            continue

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
    #Clear mouseDown 
    pyautogui.mouseUp(button='left')
    #Sleep function becouse game need time to throw float
    time.sleep(2)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
    time.sleep(5)
    floatMatching()