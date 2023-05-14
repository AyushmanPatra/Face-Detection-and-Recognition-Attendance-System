from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from student import Student
from train import Train
from face_recognition import Face_Recognition
import os
from attendence import Attendance
from developer import Developer
from help import Help
import tkinter
from time import strftime
from  datetime import datetime

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x770+0+0")  
        self.root.title("Face Recognition System")
        
        #first image
        
        
        img = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\MUJ.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root, image =self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        
        img1 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\MUJ.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root, image =self.photoimg)
        f_lbl.place(x=500,y=0,width=550,height=130)
        
        
        #Third image
        
        img2 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\MUJ.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root, image =self.photoimg)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        #BG IMAGE
        
        
        img3 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\bgitis.jpg")
        img3=img3.resize((1370,510),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root, image =self.photoimg3)
        bg_img.place(x=0,y=130,width=1290,height=510)
        
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION    ATTENDANCE SYSTEM",font=("time new roman",28,"bold"),bg="pink",fg="black")
        title_lbl.place(x=0,y=0,width=1310,height=45)
        
        
        #time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl = Label(title_lbl,font=('times new roman',14,'bold'),background='pink',foreground='black')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        
        #student button
        
        
        img4 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\b1.jpg")
        img4=img4.resize((190,179),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=163,height=180)
        
        b1_1=Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=250,width=163,height=40)
         
        
        
        # Detect face button
        
        
        img5 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\b2.png")
        img5=img5.resize((184,175),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img, image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=450,y=100,width=163,height=180)
        
        b1_1=Button(bg_img, text="Face Detector",cursor="hand2",command=self.face_data,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=250,width=163,height=40)
        
        #attendence  button
        
        
        img6 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\b3.jpeg")
        img6=img6.resize((184,175),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=100,width=163,height=180)
        
        b1_1=Button(bg_img, text="Attendence",cursor="hand2",command=self.attendance_data,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=250,width=163,height=40)
        
        
        
        #help  button
        
        
        img7 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\help.jpg")
        img7=img7.resize((184,175),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img, image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=950,y=100,width=163,height=180)
        
        b1_1=Button(bg_img, text="Helps",cursor="hand2",command=self.help_data ,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=950,y=250,width=163,height=40)
        
        
        #------------------Train  button-----------
        
        
        img8 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\train.PNG")
        img8=img8.resize((184,175),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img, image=self.photoimg8,cursor="hand2",command=self.train_data )
        b1.place(x=200,y=310,width=163,height=180)
        
        b1_1=Button(bg_img, text="Train Data",cursor="hand2",command=self.train_data ,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=450,width=163,height=40)
        
        
        
        
        #------------------Photos button------------------
        
        
        img9 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\photos.PNG")
        img9=img9.resize((184,175),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img, image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=450,y=310,width=163,height=180)
        
        b1_1=Button(bg_img, text="Photos",cursor="hand2",command=self.open_img,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=450,width=163,height=40)
        
        
        #------------------------Developer button---------------
        
        
        img10 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\developer.jpg")
        img10=img10.resize((184,175),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img, image=self.photoimg10,cursor="hand2", command=self.developer_data)
        b1.place(x=700,y=310,width=163,height=180)
        
        b1_1=Button(bg_img, text="Developer",cursor="hand2",command=self.developer_data ,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=450,width=163,height=40)
        
        
        #------------------------Exit button---------------------
        
        
        img11 = Image.open(r"Photos\exit.jpg")
        img11=img11.resize((184,175),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img, image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=950,y=310,width=163,height=180)
        
        b1_1=Button(bg_img, text="Exit",cursor="hand2",command=self.iExit,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=950,y=450,width=163,height=40)
        
        
    
    def open_img(self):
        os.startfile("data")
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
            
        
        
        
 #====================Function button======================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
            
        
        
         
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()