from tkinter import *    
import random
import string
root= Tk()  
root.geometry("600x300")
root.title("Password Generator")
character=IntVar()  
password=StringVar()  
strlist=string.ascii_letters+string.digits+string.punctuation

def value():
    ch=character.get()
    pass_word=" "
    for j in range(0,int(ch),1):
        pass_word=random.choice(strlist)+pass_word
    password.set(pass_word)
                               
#frame
frame1=Frame(root)  
frame1.grid()

#label
label1=Label(frame1,text="Password Generator",font="50")  
label1.grid(row=0,pady=10)

label2=Label(frame1,text="Number of characters in password:",font="50") 
label2.grid(row=2,column=0,pady=10)

#entry widget for number of characters
number=Entry(frame1,font="50",textvariable=character)  
number.grid(row=2,column=10,pady=10)

#button
b1=Button(frame1,bg="grey",fg="black",text="submit",command=value)  
b1.grid(row=2,column=12,pady=10)

#label
label3=Label(frame1,text="Password:",font="50")  
label3.grid(row=4,column=0,pady=10)

#entry widget for password
word=Entry(frame1,font="50",textvariable=password) 
word.grid(row=4,column=10,pady=10)

root.mainloop()
 
