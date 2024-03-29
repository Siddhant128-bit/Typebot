import pytesseract
import pyautogui
import keyboard
import cv2
import numpy as np
import imutils
from PIL import Image
import time
import os

#If you are downloading tesseract.exe please download version above 5.0.0

pytesseract.pytesseract.tesseract_cmd = r'ocr_dir\tesseract.exe'
def type():
    typer=True

    while typer:
        if keyboard.is_pressed('Enter'):
            time.sleep(0.5)
            with open('text_given.txt','r+')as f:
                data=f.readlines()
            data = ' '.join([d.strip() for d in data])
            print('Typing Text: ')
            print(data)
            for indx,i in enumerate(data):
                pyautogui.press(i,_pause=False)
                #Adding th is piece of code to bypass the latest patch by the site.
                if indx%5==0:
                    time.sleep(0.025)
                ##################################################################
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
    image=cv2.resize(image, (image.shape[1]*2,image.shape[0]*2), interpolation = cv2.INTER_AREA)
    image=cv2.bilateralFilter(image,9,175,175)
    image= cv2.bitwise_not(image)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    data=pytesseract.image_to_string(image)
    data=str(data)
    if '|' or '| ' in data:
        data=data.replace('|','I')
        data=data.replace('| ','I')
    print('Extracted Text: ')
    print(data)
    with open('text_given.txt','w+')as f:
        f.writelines(data)

    type()



def main_code():
    os.system('cls')
    run=True
    print('Press [ on top left and ] on buttom right')
    flag1=0
    flag2=0
    flagR=0
    while run:
        if keyboard.is_pressed('['):
            init=pyautogui.position()
            flag1=1

        if keyboard.is_pressed(']'):
            final=pyautogui.position()
            flag2=1

        if keyboard.is_pressed('Ctrl'):
            print('Restarting')
            flagR=1
            run=False
            return flagR

        if keyboard.is_pressed('Esc'):
            
            flagR=0
            print('Exiting')
            run=False
            return flagR

        if flag1==1 and flag2==1:
            print('Image phase begin')
            #try:
            takeimage(init,final)
            flagR=1
            run=False
  #          except:
  #              print('Error')
  #              flagR=1
  #              run=False
            return flagR


flagR=main_code()
while flagR==1:
    flagR=main_code()