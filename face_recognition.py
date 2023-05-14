from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
import cv2
from time import strftime
from  datetime import datetime
import numpy as np
from PIL import ImageTk

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x770+0+0")  
        self.root.title("Face Recognition System")
        
        
        #label
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("time new roman",28,"bold"),bg="white",fg="GREEN")
        title_lbl.place(x=0,y=0,width=1310,height=40)
        
        
        
    
        #img_left
        
        img_right = Image.open(r"Photos\AAAA.png")
        img_right=img_right.resize((1271,646),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(self.root, image =self.photoimg_right)
        f_lbl.place(x=0,y=40,width=1271,height=646)
        
        
        #button
        
        b1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.feac_recog,font=("time new roman",15,"bold"),bg="green",fg="white")
        b1.place(x=850,y=321,width=170,height=56)
    
    
    #========attendence==========================
    
    def mark_attendence(self,i,r,d):
        with open("attendencesheet.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list ) and (r not in name_list ) and (d not in name_list )):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{d},{dtString},{d1},Present")
                
            
    
    
    
    #=================face recognition===========
    
    def feac_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict= clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="psanindita@72896",database="face_recognizer")
                my_cursor=conn.cursor()
                
                # #name
                
                # my_cursor.execute("select Name from Student where studentid="+str(id))
                
                # i=my_cursor.fetchone()
                # i="+".join(i)
                
                # #select Name from students where studentid=
                
                # #student id
                # my_cursor.execute("select studentid from Student where  studentid="+str(id))
                
                # r=my_cursor.fetchone()
                # r="+".join(r)
                
                
                # #department
                # my_cursor.execute("select Dep from Student where  studentid="+str(id))
                
                # d=my_cursor.fetchone()
                # d="+".join(d)
                
                
                
                
                
                
                
                #name
                my_cursor.execute("select Name from Student where studentid="+str(id))
                result = my_cursor.fetchone()
                if result:
                    i = result[0]
                else:
                    i = "Unknown"
                
                #student id
                my_cursor.execute("select studentid from Student where  studentid="+str(id))
                result = my_cursor.fetchone()
                if result:
                    r = result[0]
                else:
                    r = "Unknown"

                #department
                my_cursor.execute("select Dep from Student where  studentid="+str(id))
                result = my_cursor.fetchone()
                if result:
                    d = result[0]
                else:
                    d = "Unknown"                    
                                
                
    
                                                
        
                if confidence>73:                               # taken 71 as confidence as of now but will change it
                     cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                     
                     cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                     
                     cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                     
                     #changing here
                     
                     self.mark_attendence(i,r,d)
                     
                else:
                    
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,y]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()
        
       
    
    

                
        
        
        
        
        
           
    
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()