import pytesseract
import pyautogui
import keyboard
import cv2
import numpy as np
import imutils
from PIL import Image
import time
import os

run=True
pytesseract.pytesseract.tesseract_cmd = r'ocr_dir\tesseract.exe'
def type():
    typer=True
    while typer:
        if keyboard.is_pressed('Enter'):
            time.sleep(0.5)
            with open('text_given.txt','r+')as f:
                data=f.readlines()
            data = ' '.join([d.strip() for d in data])
            print(data)
            for i in data:
                pyautogui.press(i,interval=0.0005,_pause=False)

            typer=False
    os.remove('text_given.txt')

def takeimage(initial,final):
    image=pyautogui.screenshot()
    x1=initial.x
    x2=final.x
    y1=initial.y
    y2=final.y
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image=image[y1-10:y2+10,x1-10:x2+10]
    cv2.imshow('image',image)
    cv2.waitKey(0)
    data=pytesseract.image_to_string(image)
    data=str(data)
    if '|' or '| ' in data:
        data=data.replace('|','I')
        data=data.replace('| ','I')
    print(data)
    with open('text_given.txt','w+')as f:
        f.writelines(data)

    type()


print('Press T on top left and B on buttom right')
flag1=0
flag2=0

while run:
    if keyboard.is_pressed('T'):
        init=pyautogui.position()
        flag1=1

    if keyboard.is_pressed('B'):
        final=pyautogui.position()
        flag2=1

    if flag1==1 and flag2==1:
        print('Image phase begin')
        takeimage(init,final)
        flag1=0
        flag2=0
