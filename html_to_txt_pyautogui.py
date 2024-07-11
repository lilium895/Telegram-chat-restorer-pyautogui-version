# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def transform_html_to_whatsapp(html_file, counting):
    
    
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract chat messages
    messages = soup.find_all('div', class_='message')

    # Transform messages to WhatsApp format
    whatsapp_chat = ''
    for message in messages:
        
        #Name of sender
        sender_element = message.find('div', class_='from_name')
        if sender_element is  not None:
            sender = sender_element.text.strip()

        #date and time
        timestamp_div = message.find('div', class_="pull_right date details")
        if timestamp_div:
            timestamp = timestamp_div['title']
            date_str = timestamp[:10]
            time_str = timestamp[11:19]
        else:
            date_str, time_str = None, None
        
        #find if it is a reply
        reply_element=message.find('div',class_='reply_to details')
        replyto = None
        if reply_element is not None:
            for number in reply_element.find_all('a'):
                replyto=number.get('href')
                
                #remove text before number of replied message
                i=replyto.index("go_to")
                replyto=replyto[i+13:]
                a=int(replyto)
                actual_message_number = message.get('id')
                i=actual_message_number.index("m")
                actual_message_number=actual_message_number[i+7:]
                b=int(actual_message_number)
                # Format reply in WhatsApp format
                if time_str:
                    whatsapp_message = f'{sender}\t{date_str}, {time_str}\t'
                    if replyto is not None:
                        whatsapp_message += f'In reply to message {a-b}\n'
                    whatsapp_chat += whatsapp_message
            
        
        #find text message
        text_element = message.find('div', class_='text')
        if text_element is not None:
            text=text_element.text.strip()
            
            # Format txt message in WhatsApp format
            if time_str:
                whatsapp_message = f'{sender}\t{date_str}, {time_str}\t'
                if text is not None:
                    whatsapp_message += f'{text}\n'
                whatsapp_chat += whatsapp_message
        #find media
        media_element=message.find('div',class_='media_wrap clearfix')
        media = None
        if media_element is not None:
            for link in media_element.find_all('a'):
                media=link.get('href')
                if 'https' not in media:
                    #remove chat_01 before file name
                    i=media.index("chat_")
                    media=media[i+8:]                
                    #remove filetype before file name
                    i=media.index("/")
                    media=media[i+1:]
                
                # Format media message in WhatsApp format
                if time_str:
                    whatsapp_message = f'{sender}\t{date_str}, {time_str}\t'
                    if media is not None:
                        if 'https' in media:
                            whatsapp_message += f'{media}\n'
                        else:
                            whatsapp_message += f'mediaelement\t{media}\n'
                            #list of media to double check if you have 'em
                            '''
                            with open('media_list.txt', 'a+', encoding='utf-8') as medialist:
                                medialist.write(f'{media}\t{media_counter}\n')
                            media_counter+=1
                            '''
                    whatsapp_chat += whatsapp_message
                                                
            
            #stickers or animation not found            
            status_emoji=media_element.find('div',class_='status details')
            if status_emoji is not None:
                sticker_emoji=status_emoji.text.strip()
                description=media_element.find('div', class_='title bold')
                whatismedia=description.text.strip()
                #check if it's a location
                if whatismedia == 'Location' or whatismedia==f'{media}':
                    continue                
                else:
                    if time_str:
                        whatsapp_message = f'{sender}\t{date_str}, {time_str}\t'
                        if sticker_emoji is not None:                            
                            whatsapp_message += f'{whatismedia}: {sticker_emoji}\n'
                            
                            whatsapp_chat += whatsapp_message
               

    # Save the transformed chat to a file
    chat_name='_chat{}.txt'.format(counting)
    with open(chat_name, 'w', encoding='utf-8') as file:
        file.write(whatsapp_chat)

    print('Transformation complete. The WhatsApp chat export is saved as {}'.format(chat_name))

# Usage example
print('Where are the html files located? Copy and paste the path of the folder in which there are the html files')
messages_path=input()
messages_path=messages_path.strip('\"')+'\\'

print('How many html files do I have to process?')
max_number=input()

# message.html
counter=1
file_path = f"{messages_path}messages.html"
transform_html_to_whatsapp(file_path,counter)

# messagesCOUNTER.html
for counter in range(max_number):
    if counter == 1 or counter == 0: continue
    file_path = f"{messages_path}messages{counter}.html"
    transform_html_to_whatsapp(file_path,counter)
