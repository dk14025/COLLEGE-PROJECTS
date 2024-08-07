from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog

mydata=[]

class Att:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1530x790+0+0")
        self.root.geometry("1280x650+0+0")
        self.root.title("Face recognition Attendance System")
        #text variable 

        
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

        #banner
        img2 = Image.open(r"images\bannerf.jpg")
        img2 = img2.resize((1280, 120), PIL.Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0, y=0, width=1280, height=120)

        img4 = Image.open(
            r"images\bg2.jpg")
        img4 = img4.resize((1280, 550), PIL.Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1280, height=550)

        title_lbl = Label(bg_img, text="ATTENDANCE RECORD", font=(
            "lucida sans typewriter", 35, "bold"), bg="darkseagreen1", fg="violetred1")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=7, y=50, width=1250, height=455)

        # left label
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=600, height=420)

        #left sub frame

        left_inside_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="", font=("times new roman", 12, "bold"))
        left_inside_frame.place(x=5, y=20, width=585, height=370)

        #label and entry

        #roll no

        roll_label = Label(left_inside_frame, text="PRN",
                           font=("times new roman", 12, "bold"))
        roll_label.grid(row=3, column=0, padx=(15, 10), pady=5)

        roll_input = ttk.Entry(left_inside_frame,textvariable=self.var_roll, width=20, font=(
            "times new roman", 12, "bold"))
        roll_input.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        #qname
        name_label = Label(left_inside_frame, text="name",
                           font=("times new roman", 12, "bold"))
        name_label.grid(row=2, column=0, padx=(15, 10), pady=5)

        name_input = ttk.Entry(left_inside_frame,textvariable=self.var_name, width=20, font=(
            "times new roman", 12, "bold"))
        name_input.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        #department
        department_label = Label(left_inside_frame, text="department",
                           font=("times new roman", 12, "bold"))
        department_label.grid(row=1, column=0, padx=(15, 10), pady=5)

        department_input = ttk.Entry(left_inside_frame, textvariable=self.var_dep, width=20, font=(
            "times new roman", 12, "bold"))
        department_input.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        #time
        time_label = Label(left_inside_frame, text="time",
                           font=("times new roman", 12, "bold"))
        time_label.grid(row=1, column=2, padx=(15, 10), pady=5)

        time_input = ttk.Entry(left_inside_frame,textvariable=self.var_time, width=20, font=(
            "times new roman", 12, "bold"))
        time_input.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        #date
        date_label = Label(left_inside_frame, text="date",
                           font=("times new roman", 12, "bold"))
        date_label.grid(row=2, column=2, padx=(15, 10), pady=5)

        date_input = ttk.Entry(left_inside_frame,textvariable=self.var_date, width=20, font=(
            "times new roman", 12, "bold"))
        date_input.grid(row=2, column=3, padx=10, pady=10, sticky=W)

       

        
       #attendance status
        attendanceLabel = Label(left_inside_frame, text="attendance status", bg="white", font=("times new roman", 12))
        attendanceLabel.grid(row=4, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame,textvariable=self.var_attend, width=20, font=("times new roman", 12), state="readonly")
        self.atten_status["values"] = ("status", "present", "absent")
        self.atten_status.grid(row=4, column=1, pady=8)
        self.atten_status.current(0)

        #buttons
        # buttonframe
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=235, width=580, height=80)

        import_btn = Button(btn_frame, text="show attendance",command=self.impcsv,  font=(
            "times new roman", 12, "bold"), bg="indianred1", fg="white", width=30)
        import_btn.grid(row=0, column=0,padx=5, pady=10)

        export_btn = Button(btn_frame, text="save attendance",command=self.exportCsv, font=(
            "times new roman", 12, "bold"), bg="darkolivegreen4", fg="white", width=30)
        export_btn.grid(row=0, column=1,padx=5, pady=10)

        # update_btn = Button(btn_frame, text="update", font=(
        #     "times new roman", 12, "bold"), bg="indianred1", fg="white", width=15)
        # update_btn.grid(row=0, column=2)

        # reset_btn = Button(btn_frame, text="reset", font=(
        #     "times new roman", 12, "bold"), bg="indianred1", fg="white", width=15)
        # reset_btn.grid(row=0, column=3)

        

        #right frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="attendance Details2", font=("times new roman", 12, "bold"))
        Right_frame.place(x=650, y=10, width=590, height=420)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=10, width=565, height=380)

        #table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attable=ttk.Treeview(table_frame,column=("PRN","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attable.xview)
        scroll_y.config(command=self.attable.yview)
        
        #column
        
        self.attable.heading("PRN",text="PRN")
        self.attable.heading("name",text="name")
        self.attable.heading("department",text="department")
        self.attable.heading("time",text="time")
        self.attable.heading("date",text="date")
        self.attable.heading("attendance",text="attendance")

        self.attable["show"]="headings"
        self.attable.column("PRN",width=100)
        self.attable.column("name",width=100)
        self.attable.column("department",width=100)
        self.attable.column("time",width=100)
        self.attable.column("date",width=100)
        self.attable.column("attendance",width=100)

        self.attable.pack(fill=BOTH,expand=1)
        self.attable.bind("<ButtonRelease>",self.get_cursor_left)

    def fetchData(self,rows):
        self.attable.delete(*self.attable.get_children())
        for i in rows:
            self.attable.insert("",END,values=i)

    def impcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export 
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  

    def get_cursor_left(self,event=""):
        cursor_focus = self.attable.focus()
        content = self.attable.item(cursor_focus)
        data = content["values"]

        
        self.var_roll.set(data[0]),
        self.var_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])  










if __name__ == "__main__":
    root = Tk()
    obj = Att(root)
    root.mainloop()