# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 18:03:26 2024 

@author: lilium895
"""
import os
import time
import pyautogui
import pyperclip


#parsing_message[0] is the sender
#parsing_message[1] is date and time
#parsing_message[2] is the text and the flag for the media element
#parsing_message[3] is the name of the media
#list_of_parsed[][] the first value is the message, the second one is the parsed data

#change to second sender
def change_to_second():
    pyautogui.moveTo(x=1492, y=604)
    pyautogui.click()
#change to first sender
def change_to_first():
    pyautogui.moveTo(x=548, y=603)
    pyautogui.click()
    
    




def write_txt(txt,date,sender):
    pyperclip.copy(txt)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.25)
    pyautogui.keyDown('shift')
    pyautogui.press('enter')
    pyautogui.keyUp('shift')
    pyperclip.copy(date)
    pyautogui.hotkey("ctrl", "v")    
    pyautogui.keyDown('shift')
    pyautogui.press('left', presses=20)
    pyautogui.keyUp('shift')
    time.sleep(0.25)
    pyautogui.hotkey('ctrl','shift','m')
    time.sleep(0.25)
    pyautogui.press('enter')
 
def search_for_media(media_name,user):
    pyautogui.click(x=1776, y=713)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('delete')
    time.sleep(1)
    pyperclip.copy(media_name)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.moveTo(x=1716, y=855)
    pyautogui.click()
    time.sleep(0.7)
    if user==1:
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(x=548, y=343, duration=1)
        pyautogui.mouseUp(button='left')
    else:
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(x=1492, y=344, duration=1)
        pyautogui.mouseUp(button='left')
    time.sleep(1)
    pyautogui.press('shift')    
    pyautogui.press('enter')
'''
IMPORTANT
REPLACE C:\\Users\\pollicino\\Desktop\\allmedia with the path of the folder where all your media are
REMEMBER TO REPLACE \ with \\
leave \\{media_name} after
'''
    media_size=os.path.getsize(f"C:\\Users\\pollicino\\Desktop\\allmedia\\{media_name}")
    if media_size < 8000000:
        time.sleep(2)
    else:
        time.sleep(120)




'''
IMPORTANT
REPLACE 'number of text files' with the last number that appear in _chat{number}
but with +1
'''

#insert the number of text files to recover

for number in range(1,number of text files):
    print(number)
    change_to_second()
    user1=3
    user2=1
'''
IMPORTANT
replace C:\\Users\\pollicino with the path of the folder in which are the _chat files
REMEMBER TO REPLACE \ with \\
leave\\_chat{number}.txt after
'''
    with open(f"C:\\Users\\pollicino\\_chat{number}.txt", 'r', encoding='utf-8') as file:
   #remove \n and makes a list of messages
       raw_messages = file.read().splitlines() 
       number_of_messages=len(raw_messages)
    list_of_parsed_messages=[]
    for element in raw_messages:
    #makes a lists of the constitutive elements of the message
        message=list(element.split("\t"))
        sender=message[0]
        date_time=message[1]
        text_or_flag=message[2]
        
        '''
        IMPORTANT
        REPLACE Sender name with the name of one of the two senders AS it is in the _chat.txt
        
        '''
        if 'Sender name' in sender:
            user1=3     
            change_to_second()
        else:
            user1=1
            change_to_first()
        if text_or_flag == 'mediaelement':
            media=message[3]
            search_for_media(media,user1)

        else:
            write_txt(text_or_flag,date_time,user1) 


