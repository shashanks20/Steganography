import cv2
import os
import string
import tkinter as tk
import tkinter.font as font

def window2():

    def encrypt(imgloc,inputtxt,inputkey):
        img = cv2.imread(imgloc)
        global mssg 
        mssg += inputtxt
        global key
        key = inputkey
        k=len(key)
        img[0,0,0] = min(len(mssg),255)
        n=1
        m=0
        z=0
        for i in range(0,len(mssg)):
            img[n,m,z] = ((d[mssg[i]]+k)%255)
            n=n+1
            m=m+1
            z=(z+1)%3
        cv2.imwrite("new1.png",img)
        os.system("start new1.png")

    base1 = tk.Tk()
    base1.geometry('500x500')
    base1.minsize(500,500)
    base1.maxsize(500,500)
    base1.title("Stegnography")  
  
    heading = tk.Label(base1, text="Encryption",width=20,font=("bold", 18))
    heading.place(x=120,y=53)  
   
    imglabel = tk.Label(base1, text="Image Address",width=20,font=("bold", 12))
    imglabel.place(x=80,y=130)  
    imgentry = tk.Entry(base1,width=22,font=('Arial 13'))  
    imgentry.place(x=240,y=130)  
    
    mssglabel = tk.Label(base1, text="Secret Message",width=20,font=("bold", 12))
    mssglabel.place(x=68,y=180) 
    inputtxt = tk.Text(base1, 
                   height = 5, 
                   width = 22,font=('Arial 13')) 
    inputtxt.place(x=240,y=180)  

 
    keylabel = tk.Label(base1, text="Key",width=20,font=("bold", 12))  
    keylabel.place(x=70,y=300)  
    keyentry = tk.Entry(base1,width=22,font=('Arial 13'))  
    keyentry.place(x=240,y=300)
    
    tk.Button(base1, text='Encrypt',width=20,bg='brown',fg='white',font=("bold", 12),
              command=lambda:encrypt(imgentry.get(),inputtxt.get("1.0",'end-1c'),keyentry.get())).place(x=180,y=350)
    base1.mainloop()

def window3():

    def decrypt(imgloc,passw):
        img1 = cv2.imread(imgloc)
        global mssg
        global key
        k=len(key)
        decrypt_mssg=""
        if(key==passw):
            n=1
            m=0
            z=0
            x=img1[0,0,0]
            for i in range(0,x):
                decrypt_mssg += c[(img1[n,m,z]-k)%255]
                n=n+1
                m=m+1
                z=(z+1)%3
            smssglabel["text"]="Secret message : "+decrypt_mssg
        else:
            smssglabel["text"]="Wrong Secret Key"
        
    base1 = tk.Tk()
    base1.geometry('500x500')
    base1.minsize(500,500)
    base1.maxsize(500,500)
    base1.title("Stegnography")

    heading = tk.Label(base1, text="Decryption",width=20,font=("bold", 18))
    heading.place(x=120,y=53) 

    imglabel = tk.Label(base1, text="Image Address",width=20,font=("bold", 12))
    imglabel.place(x=80,y=130) 
    imgentry = tk.Entry(base1,width=22,font=('Arial 13'))  
    imgentry.place(x=240,y=130)  

    keylabel = tk.Label(base1, text="Key",width=20,font=("bold", 12))  
    keylabel.place(x=68,y=180)  
    keyentry = tk.Entry(base1,width=22,font=('Arial 13'))  
    keyentry.place(x=240,y=180)
    
    tk.Button(base1, text='Decrypt',width=20,bg='brown',fg='white',font=("bold", 12),
              command=lambda:decrypt(imgentry.get(),keyentry.get())).place(x=180,y=250)  

    smssglabel = tk.Label(base1, text="",wraplength=300,font=("bold", 12))  
    smssglabel.place(x=110,y=300)
    base1.mainloop()
        
root = tk.Tk()

root.title("Stegnography")
root.geometry("800x400")
root.minsize(700,250)
root.maxsize(700,250)

heading = tk.Label(root, text="Image Stegnography",width=20,font=("bold", 20))  
heading.place(x=200,y=53) 


tk.Button(root, text="Encrypt",width=10,height=2,bg="purple",fg="white",font=("bold", 10), command=window2).place(x=220,y=150)
tk.Button(root, text="Decrypt",width=10,height=2,bg="green",fg="white",font=("bold", 10), command=window3).place(x=320,y=150)
tk.Button(root, text="Quit",width=10,height=2,bg="white",fg="black",font=("bold", 10), command=quit).place(x=420,y=150)


key="shashu"
mssg=""
d={}
c={}       
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)
root.mainloop()