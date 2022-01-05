import numpy as np
import cv2 as cv
import time
from pynput import mouse
import pyautogui
from PIL import ImageGrab
from pynput.mouse import Controller, Button
import win32gui, win32ui, win32con

while(True): 
    pos =pyautogui.position()
    print(pos)