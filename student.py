from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x770+0+0")  
        self.root.title("Face Recognition System")
        
        #variables
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        #self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
       # self.var_address=StringVar()
        self.var_teacher=StringVar()
      
      
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
        
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("time new roman",28,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1310,height=40)
        
        
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=45,width=1270,height= 620)
        
        
        #left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=640,height=500)
        
        
        #Left label image
        
        img_left = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\MUJ1.jpg")
        img_left=img_left.resize((640,130),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame, image =self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=120)
        
        #current course information
        
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Infromation",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=120,width=720,height=137)
        
        
        #DEPARTMENT
        
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CS","IT","CCE","DATA SCIENCE","CIVIL","MECHANICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #COURSE
        
        course_label=Label(current_course_frame,text="Section",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Section","A","B","C","D","E","F")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
        #YEAR
        
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #semester
        
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        
        #Class Student information
        
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=228,width=720,height=500)
        
        #Student ID
        
        studentId_label=Label(class_student_frame,text="Registration ID",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=4,sticky=W)
        
        #Student_Name
        
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=4,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5,pady=4,sticky=W)
        
        
        #Gender
        
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=5,pady=4,sticky=W)
        
        gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        gender_entry.grid(row=1,column=1,padx=5,pady=4,sticky=W)
        
        
        
        #Email
        
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=1,column=2,padx=5,pady=4,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=1,column=3,padx=5,pady=4,sticky=W)
        
        #Phone Number
        
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=2,column=0,padx=5,pady=4,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=2,column=1,padx=5,pady=4,sticky=W)
        
        
        #ClassCoordinator
        
        classcoor_label=Label(class_student_frame,text="Coordinator Name:",font=("times new roman",12,"bold"),bg="white")
        classcoor_label.grid(row=2,column=2,padx=5,pady=4,sticky=W)
        
        classcoor_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        classcoor_entry.grid(row=2,column=3,padx=5,pady=4,sticky=W)
        
        #radio buttons
        self.var_radio1=StringVar()
        
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="yes")
        radiobtn1.grid(row=5,column=0)
        
        
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=5,column=1)
        
        # buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=130,width=715,height=40)
        #save button 
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=11,font=("times newn roman",9,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        #update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data, width=11,font=("times newn roman",9,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        #delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,  width=11,font=("times newn roman",9,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        #reset button
        reset_btn=Button(btn_frame,text="Reset",width=11,font=("times newn roman",9,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        
        #photo sample button
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo Sample ",width=16,font=("times newn roman",9,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=4)
        
        #update photo sample
        take_photo_btn=Button(btn_frame,text="Update Photo Sample ",width=20,font=("times newn roman",9,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=5)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Right label frame
        
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),width=17)
        Right_frame.place(x=640,y=10,width=610,height=451)
        
        
        img_right = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\student-banner (1).jpg")
        img_right=img_right.resize((640,130),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame, image =self.photoimg_right)
        f_lbl.place(x=0,y=0,width=700,height=100)
        
        #==========Search System=========
        
        
        
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=103,width=603,height=65)
        
        
        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=4,pady=4,sticky=W)
       
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=13)
        search_combo["values"]=("Select","Registration no","Section")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=1,pady=10,sticky=W)
        
        
        #search entry
        
        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=4,sticky=W)
        
        
        #Search Button
        
        search_btn=Button(search_frame,text="Search",width=15,font=("times newn roman",9,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)
        
        
        #ShowAll Button
        
        showAll_btn=Button(search_frame,text="Show All",width=15,font=("times newn roman",9,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3)
        
        #=========Table frame===============
        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=170,width=598,height=256)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","year","sec","sem","reg","gender","phone","name","email","cname"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("year",text="Section")
        self.student_table.heading("sec",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("reg",text="Registration Number")
        self.student_table.heading("gender",text="Name")        #error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        self.student_table.heading("phone",text="Gender")
        self.student_table.heading("name",text="Gmail")         #error!!!!!!!!!!!!!!!!!!!!!!!!111
        self.student_table.heading("email",text="Phone Number")
        self.student_table.heading("cname",text="Coordinator Name")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=90)
        self.student_table.column("year",width=80)
        self.student_table.column("sec",width=60)
        self.student_table.column("sem",width=80)
        self.student_table.column("reg",width=130)
        self.student_table.column("gender",width=140)
        self.student_table.column("phone",width=140)
        self.student_table.column("name",width=195)
        self.student_table.column("email",width=150)
        self.student_table.column("cname",width=140)
        
        
        #pack
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_Data()
        
        #==================function declaration=============
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="psanindita@72896",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                  self.var_dep.get(),
                                                                                                  self.var_course.get(),
                                                                                                  self.var_year.get(),
                                                                                                  self.var_semester.get(),
                                                                                                  self.var_std_id.get(),
                                                                                                  self.var_std_name.get(),
                                                                                                  self.var_gender.get(),
                                                                                                  self.var_email.get(),
                                                                                                  self.var_phone.get(),
                                                                                                  self.var_teacher.get(),
                                                                                                  self.var_radio1.get(),
                    
                                                                                                 ))
                
                conn.commit()
                self.fetch_Data
                conn.close()
                messagebox.showinfo("Sussess","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
 
 
 #==============fetch data================================

    def fetch_Data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="psanindita@72896",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 
    
    #===============get cursor=========================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_email.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_teacher.set(data[9]),
        self.var_radio1.set(data[10]),
      
      
      
      
      
      
      
      
        
    
    #====================update function=============(Some Error is coming)
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this Student Details",parent=self.root)
                if Update > 0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="psanindita@72896",database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update Student set Dep=%s,Course=%s,Year=%s,Semester=%s,studentid=%s,Name=%s,Gender=%s,Email=%s,Phone=%s,Teacher=%s,PhotoSample=%s where studentid=%s", (
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get(), 
                                                                                                        self.var_std_id.get()
                                                                                    ))
                
                else:
                    if not Update:
                     return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_Data()
                conn.close()
            
            
            except Exception as es:
             messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
   
   

    
    
    
    
    #=======================Delete Function========================================================
    
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID Must be Required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student info",parent=self.root)
                if delete >0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="psanindita@72896",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where studentid=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_Data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted Student Details",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                        
        
        
        
#===================reset(Bad mai Karugaaa)==========
    
                    
    def reset_data(self):
        self.var_dep.set("Select Department")
           
  










#====================Generate data set or take photo sample========
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="psanindita@72896",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                # my_cursor.execute("update Student set Dep=%s,Course=%s,Year=%s,Semester=%s,studentid=%s,Name=%s,Gender=%s,Email=%sPhone=%s,Teacher=%s,PhotoSample=%s where studentid=%s", (
                #                                                                                         self.var_dep.get(),
                #                                                                                         self.var_course.get(),
                #                                                                                         self.var_year.get(),
                #                                                                                         self.var_semester.get(),
                #                                                                                         self.var_std_name.get(),
                #                                                                                         self.var_gender.get(),
                #                                                                                         self.var_email.get(),
                #                                                                                         self.var_phone.get(),
                #                                                                                         self.var_teacher.get(),
                #                                                                                         self.var_radio1.get(), 
                #                                                                                         self.var_std_id.get()==id+1
                #                                                             ))
                
                
                
                
                my_cursor.execute("update Student set Dep=%s,Course=%s,Year=%s,Semester=%s,studentid=%s,Name=%s,Gender=%s,Email=%s,Phone=%s,Teacher=%s,PhotoSample=%s where studentid=%s", (
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get(), 
                                                                                                        self.var_std_id.get()==id+1
                                                                            ))

                conn.commit()
                self.fetch_Data()
                self.reset_data()
                conn.close()
                #load predifined data on face frontals from open cv
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #convert img to greay
                    faces=face_classifier.detectMultiScale(gray,1.3,5) 
                    #scealing factor = 1.3
                    #minimum neighbor= 5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(600,600))  #earlier was 450,450
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        #file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        file_name_path = "data/user." + str(self.var_std_id.get()) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                        cv2.imshow("Crooped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generate data sets compled !!!!")
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)        
                
                
                
                
                
                
                
                
                    
                    
                    


        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()