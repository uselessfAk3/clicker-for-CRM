import pyautogui as pag
import time
import pyperclip, keyboard

def clicker(phone_number, name_of_client):
    pag.FAILSAFE = False
    # print(pag.position())
    pag.click(1704, 107, 1, 0, 'left') # Create form
    pag.click(950, 488, 1, 1, 'left') #name_of_phone field
    pag.typewrite(phone_number, 0.0000001) #write phone_number
    pag.sleep(13)
    pag.click(935, 589, 1, 0.1, 'left') #name field
    type(name_of_client, 0.0000001)
    pag.click(820, 776, 1, 1, 'left') #DALEE

def paste(text: str):
    buffer = pyperclip.paste()
    pyperclip.copy(text)
    keyboard.press_and_release('ctrl + v')
    pyperclip.copy(buffer)

def type(text: str, interval=0.0):
   if interval == 0.0:
       paste(text)
       return

   buffer = pyperclip.paste()
   for char in text:
       pyperclip.copy(char)
       keyboard.press_and_release('ctrl + v')
       time.sleep(0.1)
   pyperclip.copy(buffer)


