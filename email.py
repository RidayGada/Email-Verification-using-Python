from tkinter import *

window=Tk()
window.title(" Free Email verification") #rename the title of windows
window.geometry("700x500")

l3=Label(window, text="                                   ", font=("Sans-serif",15), bg="#3498db", fg="#ffffff",bd=15)
l3.place(x=50, y=350)

l1=Label(window, text="Enter your Email in the input box below : " , font=("Sans-serif",15), bg="#3498db", fg="#ffffff",bd=15)
l1.place(x=70 ,y=60)

v=StringVar()

inputbox1=Entry(window,width=50, font=("Sans-serif",10), bg="#3498db", fg="#ffffff", bd=15, textvariable=v)
inputbox1.place(x=70, y=150)

def clicked():
    email=v.get()
    k = 0
    j = 0
    m = 0
    #email = input("Enter your Email :")  # g@g.in
    if len(email) >= 6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@") == 1):
                if (email[-4] == ".") ^ (email[-3] == "."):
                    for i in email:
                        if i == " ":
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                    if k == 1 or j == 1:
                        ans="Wrong Email, there cannot be space and Uppercase letters in email ID   "
                        k=2
                else:
                    ans="Wrong Email, format of email must be either 'a@b.com' or 'c@d.in'     "
                    k=2
            else:
                ans="Wrong Email, symbol '@' can be used only once in email ID      "
                k=2
        else:
            ans="Wrong Email, first element of email ID must be an alphabet   "
            k=2
    else:
        ans="Wrong Email, email should have a minimum length of 6      "
        k=2

    if k==2:
        pass
    elif k==0:
        ans="Correct Email    "
        
    l3.config(text=ans)

button=Button(window, text="Verify",font=("Sans-serif",15), bg="#3498db", fg="#ffffff", bd=15, command=clicked)
button.place(x=230, y=250)

window.mainloop()
