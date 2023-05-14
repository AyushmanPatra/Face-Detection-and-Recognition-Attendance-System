from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
import cv2
import os
import numpy as np
from PIL import ImageTk



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x770+0+0")  
        self.root.title("Face Recognition System")
        
        #label
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("time new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1310,height=40)
        
        
        
        #img_top
        
        img_top = Image.open(r"Photos\MUJ.jpg")
        img_top=img_top.resize((1320,220),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root, image =self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1320,height=250)
        
        
        
        
        
        #button
        
        b1=Button(self.root,text="TRAIN DATA",command=self.train_classifier ,cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=0,y=290,width=1300,height=60)
        
        
        #img_down
        
        img_buttom = Image.open(r"Photos\photos.png")
        img_buttom=img_buttom.resize((1320,340),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg_button=ImageTk.PhotoImage(img_buttom)
        
        f_lbl=Label(self.root, image =self.photoimg_button)
        f_lbl.place(x=0,y=360,width=1320,height=345)
        
        
    def train_classifier (self):
        data_dir=("data")  #take data from data directory
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] #list comprensing
           
        faces=[]
        ids=[]
        #griding the images
        for image in path:
            img=Image.open(image).convert('L') #greay scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            #--------------------------1----------.----1
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Tranning",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #===============train the classifier======
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets comleted!!")
        
        
        
        
            
              
            
        
        
        
        
            
    
    





        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()