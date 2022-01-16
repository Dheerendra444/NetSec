

#importing required packages for creating GUI
from tkinter import *
from tkinter import ttk

#creating string variable to store alphabets.
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Initializing Tkinter and creating window.
root = Tk()

#createing window title.
root.title('Encryption Decryption UI by using Caesar Cipher')

#Allowing window to be resized.
root.resizable(True,True)

#giving color to window background.
root.configure(background='black')

#creating frame and provide text and styling.
root.frame_header = ttk.Frame()
ttk.Label(root.frame_header, text = 'Caesar Cipher', style = 'Header.TLabel').grid(row = 0, column = 1)
ttk.Label(root.frame_header, text = 'Enter Number (1-25):', style = 'Header.TLabel').grid(row = 2, column = 0)
ttk.Label(root.frame_header, text = 'Text:', style = 'Header.TLabel').grid(row = 4, column = 0)
ttk.Label(root.frame_header, text='Encrypted/Decrypted Text:',style='Header.TLabel').grid(row=8, column=0)

#seperating the .grid as it was causing a None type error.
enc_dec_text = ttk.Entry(root.frame_header, width=110)
enc_dec_text.grid(row=8,column=1)

#creating cipher shift drop down button.
cipher_shift_menu = StringVar()
Spinbox(root.frame_header,from_=1, to=25, textvariable=cipher_shift_menu).grid(row=2, column=1)

#now starts text entry.
#seperating the .grid as it was causing a None type error.
text_entry = ttk.Entry(root.frame_header, width=100)
text_entry.grid(row=4,column=1)

#function for encryption.
def encrypt_text():
    stringtoencrypt = text_entry.get()
    stringtoencrypt = str(stringtoencrypt)
    stringtoencrypt=stringtoencrypt.upper()
    ciphershift = cipher_shift_menu.get()
    ciphershift=int(ciphershift)
    stringencrypted=""
    for character in stringtoencrypt:
        position = letters.find(character)
        newposition = position+ciphershift
        if character in letters:
            stringencrypted = stringencrypted + letters[newposition]
        else:
            stringencrypted = stringencrypted + character
    enc_dec_text.insert(0, stringencrypted)

#function for decryption.
def decrypt_text():
    stringtodecrypt = text_entry.get()
    stringtodecrypt = str(stringtodecrypt)
    stringtodecrypt=stringtodecrypt.upper()
    ciphershift = cipher_shift_menu.get()
    ciphershift=int(ciphershift)
    stringdecrypted=""
    for character in stringtodecrypt:
        position = letters.find(character)
        newposition = position-ciphershift
        if character in letters:
            stringdecrypted = stringdecrypted + letters[newposition]
        else:
            stringdecrypted = stringdecrypted + character  
    enc_dec_text.insert(0, stringdecrypted)

#Adding buttons to encrypt or decrypt
encrypt_button = ttk.Button(root.frame_header,text='Encrypt',command = lambda: encrypt_text()).grid(row=6,column=0)
decrypt_button = ttk.Button(root.frame_header,text='Decrypt',command = lambda: decrypt_text()).grid(row=6,column=1)

root.frame_header.pack()

#We use the mainloop() method when we want to run our program.
root.mainloop()
