from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x770+0+0")  
        self.root.title("Face Recognition System")
        
        
      
        
        
        
       #BG IMAGE
        
        
        img3 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\bgitis.jpg")
        img3=img3.resize((1370,510),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root, image =self.photoimg3)
        bg_img.place(x=0,y=130,width=1290,height=510)
        
        
        #img_top
        
        img_top = Image.open(r"Photos\MUJ.jpg")
        img_top=img_top.resize((1320,250),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root, image =self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1320,height=250)
        
        
        #label
        title_lbl=Label(self.root,text="DEVELOPER",font=("time new roman",28,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1310,height=40)
        
        #AYUSHMAN
        
        img1 = Image.open(r"Photos\dev1.jpeg")
        img1=img1.resize((398,357),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        b1=Button(bg_img, image=self.photoimg1,cursor="hand2")
        b1.place(x=170,y=150,width=400,height=300)
        
        b1_1=Button(bg_img, text="AYUSHMAN PATRA",cursor="hand2",font=("time new roman",15,"bold"),bg="white",fg="BLACK")
        b1_1.place(x=170,y=401,width=400,height=80)
        
        
        #SWATI
        
        img4 = Image.open(r"Photos\dev2.jpeg")
        img4=img4.resize((395,405),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img, image=self.photoimg4,cursor="hand2")
        b1.place(x=730,y=150,width=400,height=300)
        
        b1_1=Button(bg_img, text="SWATI JAIN",cursor="hand2",font=("time new roman",15,"bold"),bg="white",fg="BLACK")
        b1_1.place(x=730,y=401,width=400,height=80)



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
        