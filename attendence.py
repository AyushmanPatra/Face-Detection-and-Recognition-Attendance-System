from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x770+0+0")  
        self.root.title("Face Recognition System")
        
        
        #========variables=====================
        
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        
        
        
        
        
        
        
        
        #first image
        
        
        img = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\MUJ.jpg")
        img=img.resize((700,150),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root, image =self.photoimg)
        f_lbl.place(x=0,y=0,width=700,height=150)
        
        #second image
        
        img1 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\MUJ.jpg")
        img1=img1.resize((500,150),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root, image =self.photoimg)
        f_lbl.place(x=700,y=0,width=700,height=150)
        
        #bg image
        
        img3 = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\bgitis.jpg")
        img3=img3.resize((1370,510),Image.ANTIALIAS)     #ANTIALIAS -it is used to covert higher level to lower level
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root, image =self.photoimg3)
        bg_img.place(x=0,y=150,width=1290,height=510)
        
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("time new roman",28,"bold"),bg="WHITE",fg="GREEN")
        title_lbl.place(x=0,y=0,width=1310,height=40)
        
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=2,y=45,width=1270,height= 620)
        
        #left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=640,height=500)
        
        # left img
        
        img_left = Image.open(r"C:\Users\ayush\OneDrive\Desktop\Face Reconisation System\Photos\MUJ1.jpg")
        img_left=img_left.resize((640,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame, image =self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=120)
        
        
        
        
        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=2,y=123,width=620,height= 230)
        #! can increas the height above
        
        
        
        #attendence id
        
        attendanceId_label=Label(left_inside_frame,text="Attendence ID",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=5,sticky=W)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id ,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=5,pady=4,sticky=W)
        
        
        #Roll
        
        rollLabel_label=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        rollLabel_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)
        
        rollLabel_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll ,width=20,font=("times new roman",12,"bold"))
        rollLabel_entry.grid(row=0,column=3,pady=8)
        
        
        
        #Name
        
        nameLabel_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        nameLabel_label.grid(row=1,column=0)
        
        nameLabel_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
        nameLabel_entry.grid(row=1,column=1,pady=8)
        
        #Department
        
        depLabel_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        depLabel_label.grid(row=1,column=2)
        
        depLabel_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
        depLabel_entry.grid(row=1,column=3,pady=8)
        
        #Time
        
        timeLabel_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        timeLabel_label.grid(row=2,column=0)
        
        timeLabel_entry=ttk.Entry(left_inside_frame,textvariable= self.var_atten_time ,width=20,font=("times new roman",12,"bold"))
        timeLabel_entry.grid(row=2,column=1,pady=8)
        
        
        #date
        
        dateLabel_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        dateLabel_label.grid(row=2,column=2)
        
        dateLabel_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date , width=20,font=("times new roman",12,"bold"))
        dateLabel_entry.grid(row=2,column=3,pady=8)
        
        #Attendence
        
        attendanceLabel_label=Label(left_inside_frame, text="Attendence",font=("times new roman",12,"bold"),bg="white")
        attendanceLabel_label.grid(row=3,column=0)
        
        attendanceLabel_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        attendanceLabel_entry.grid(row=2,column=3,pady=8)
        
        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly",width=20)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,pady=10,sticky=W)
        
        
        #button frame
        
    
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=70)
        
        #import csv button 
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv ,width=21,font=("times newn roman",9,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        #Export csv button
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv, width=21,font=("times newn roman",9,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        #update csv button
        delete_btn=Button(btn_frame,text="Update csv",  width=21,font=("times newn roman",9,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        #reset csv button
        reset_btn=Button(btn_frame,text="Reset csv",width=21,command=self.reset_data,font=("times newn roman",9,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Right label frame
        
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),width=17)
        Right_frame.place(x=640,y=10,width=610,height=451)
        
        #button frame
        
    
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=594,height=390)
        
        #======scroll bar table
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("name","roll","department","time","date","attendance","id"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)
        
        
        
        self.AttendenceReportTable.heading("name",text="NAME")
        self.AttendenceReportTable.heading("id",text="ATTENDANCE ID")
        self.AttendenceReportTable.heading("roll",text="ROLL")
        
        self.AttendenceReportTable.heading("department",text="DEPARTMENT")
        self.AttendenceReportTable.heading("time",text="TIME")
        self.AttendenceReportTable.heading("date",text="DATE")
        self.AttendenceReportTable.heading("attendance",text="ATTENDANCE")
        
        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendance",width=100)
        
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
        

        #ftech data
        
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)
       
       
       #IMPORT CSV
            
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open CVS',filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln)as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
            
    #EXPORT CSV
            
            
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Open CVS',filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your, data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    def get_cursor(self, event=""):
        cursor_row =self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[1])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[0])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows[5])
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()