from tkinter import *
from tkinter import messagebox
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            cipher += ' '
    return cipher 
def decrypt(message): 
    message += ' '
    decipher = '' 
    citext = '' 
    for letter in message: 
        if (letter != ' '): 
            i = 0
            citext += letter 
        else: 
            i += 1
            if i == 2 : 
                decipher += ' '
            else: 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = '' 
    return decipher     
optionlist=["String", "Morse Code"]
root=Tk()
root.geometry("390x80")
root.resizable(0,0)
root.title("Morse Code Translator")
message=StringVar(root)
option=StringVar(root)
option.set(optionlist[0])
output=StringVar(root)
output.set("")
message.set("")
op_list = OptionMenu(root, option, *optionlist).grid(row=0, column=1, columnspan=2)
Label(root, text="Output").grid(row=2, column=0)
Label(root, text="Text", width=10).grid(row=1, column=0)
Label(root, text="From", width=10).grid(row=0, column=0)
entry1 = Entry(root, textvariable=message, width=50)
entry1.grid(column=2, row=1)
entry2 = Entry(root, textvariable=output, width=50, state="readonly").grid(row=2, column=1,columnspan=2)
def message_change(*args):
    msg=message.get()
    if option.get()=="String":
        try:
            output.set(encrypt(msg.upper()))
        except KeyError:
            messagebox.showerror("Error", "Unconvertable Character Entered")
            message.set(msg[:-1])
    else:
        if msg=="":
            output.set("")
        elif msg[-1]=="-" or msg[-1]=="." or msg[-1]==" ":
            try:
                output.set(decrypt(msg))
            except UnboundLocalError and ValueError:
                messagebox.showerror("Error", "Can't Convert this Morse Character")
                message.set(msg[:-1])
        else:
            messagebox.showerror("Error", "Invalid Morse Character")
            message.set(message.get()[:-1])   
def changeoption(*args):
    message.set("")
    output.set("")
option.trace("w", changeoption)        
message.trace("w", message_change)
root.mainloop()
