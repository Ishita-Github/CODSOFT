from tkinter import *
import random
root=Tk()
root.geometry("1000x800")
root.title("ROCK-PAPER-SCISSORS")
root.config(bg="turquoise")

#frame
f1=Frame(root,width=600,height=300)
f1.pack(pady=40)

f2=Frame(root,width=800,height=300)
f2.pack(pady=20)

f3=Frame(root,width=800,height=300)
f3.pack(pady=20)

user_choice= StringVar()
computer_choice=StringVar()
winner=StringVar()
option=["ROCK","PAPER","SCISSORS"]

def rock():
    user_choice.set("ROCK")
    choice=random.choice(option)
    computer_choice.set(choice)
    if choice=="ROCK":
        winner.set("TIE")
    elif choice=="SCISSORS":
        winner.set("USER")
    else:
        winner.set("COMPUTER")

def paper():
    user_choice.set("PAPER")
    choice=random.choice(option)
    computer_choice.set(choice)
    if choice=="PAPER":
        winner.set("TIE")
    elif choice=="ROCK":
        winner.set("USER")
    else:
        winner.set("COMPUTER")

def scissors():
   user_choice.set("SCISSORS")
   choice=random.choice(option)
   computer_choice.set(choice)
   if choice=="SCISSORS":
        winner.set("TIE")
   elif choice=="PAPER":
        winner.set("USER")
   else:
        winner.set("COMPUTER")

    
#buttons
b1=Button(f1,text="Rock",font="TimesNewRoman 20",width=8,height=2,bg="black",fg="white",command=rock)
b1.pack(side="left",pady=100,padx=20)
b2=Button(f1,text="Paper",font="TimesNewRoman 20",width=8,height=2,bg="black",fg="white",command=paper)
b2.pack(side="left",pady=100,padx=20)
b3=Button(f1,text="Scissors",font="TimesNewRoman 20",width=8,height=2,bg="black",fg="white",command=scissors)
b3.pack(side="left",pady=100,padx=20)

#label
label1=Label(f2,text="User Choice:",font="TimesNewRoman 20")
label1.pack(pady=25,padx=10,side="left")

label2=Label(f2,textvariable=user_choice,font="TimesNewRoman 20")
label2.pack(pady=25,padx=10,side="left")

label3=Label(f2,text="Computer's Choice:",font="TimesNewRoman 20")
label3.pack(pady=25,padx=10,side="left",anchor="sw")

label4=Label(f2,textvariable=computer_choice,font="TimesNewRoman 20")
label4.pack(pady=25,padx=10,side="right")

#announcing winner

label5=Label(f3,text="Winner:",font="TimesNewRoman 20")
label5.pack(pady=10,padx=10,side="left")

label6=Label(f3,textvariable=winner,font="TimesNewRoman 20")
label6.pack(pady=10,padx=10,side="right")

root.mainloop()

