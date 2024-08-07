from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2


class Attendance:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1530x790+0+0")
        self.root.geometry("1280x650+0+0")
        self.root.title("Face recognition Attendance System")

        # var
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_batch = StringVar()
        self.var_photo = StringVar()

        # banner
        img2 = Image.open(
            r"images\bannerf.jpg")
        img2 = img2.resize((1280, 120), PIL.Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=0, y=0, width=1280, height=120)

        # img1 = Image.open(r"C:\Users\Deb Pattanayak\OneDrive\Desktop\face_recog_attendance\images\logo.png")
        # img1 = img1.resize((300, 120), PIL.Image.LANCZOS)
        # self.photoimg1=ImageTk.PhotoImage(img1)
        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=0, y=0, width=300, height=120)

        # #banner2
        # img2 = Image.open(r"C:\Users\Deb Pattanayak\OneDrive\Desktop\face_recog_attendance\images\banner.jpg")
        # img2 = img2.resize((630, 120), PIL.Image.LANCZOS)
        # self.photoimg2=ImageTk.PhotoImage(img2)
        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=310, y=0, width=600, height=120)

        # #banner3
        # img3 = Image.open(r"C:\Users\Deb Pattanayak\OneDrive\Desktop\face_recog_attendance\images\logo.png")
        # img3 = img3.resize((300, 120), PIL.Image.LANCZOS)
        # self.photoimg3=ImageTk.PhotoImage(img3)
        # f_lbl=Label(self.root,image=self.photoimg3)
        # f_lbl.place(x=920, y=0, width=300, height=120)

        # background
        img4 = Image.open(
            r"images\bg2.jpg")
        img4 = img4.resize((1280, 550), PIL.Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1280, height=550)

        title_lbl = Label(bg_img, text="STUDENT DATA", font=(
            "lucida sans typewriter", 35, "bold"), bg="darkseagreen1", fg="violetred1")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=7, y=50, width=1250, height=455)

        # left label
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=600, height=420)

        # current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current course information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=5, width=585, height=120)

        # department

        dep_label = Label(current_course_frame, text="Department",
                          font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=(15, 10), pady=10)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), width=15, state="readonly")
        dep_combo["values"] = ("select", "CE", "IT", "EXTC", "AIDS", "AIML")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=2, sticky=W)

        # year
        year_label = Label(current_course_frame, text="Year",
                           font=("times new roman", 12, "bold"))
        year_label.grid(row=0, column=2, padx=(30, 10), pady=10)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), width=15, state="readonly")
        year_combo["values"] = ("select year", "FE", "SE", "TE", "BE")
        year_combo.current(0)
        year_combo.grid(row=0, column=3, padx=2, pady=2, sticky=W)

        # semester
        sem_label = Label(current_course_frame, text="semester",
                          font=("times new roman", 12, "bold"))
        sem_label.grid(row=1, column=0, padx=10, pady=10)

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=(
            "times new roman", 12, "bold"), width=15, state="readonly")
        sem_combo["values"] = ("select semester", "1",
                               "2", "3", "4", "5", "6", "7", "8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=1, padx=2, pady=2, sticky=W)

       # student detail frame 2/2 l
        sd_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                              text="student details", font=("times new roman", 12, "bold"))
        sd_frame.place(x=5, y=130, width=585, height=260)

        # student name
        name_label = Label(sd_frame, text="name", font=(
            "times new roman", 12, "bold"))
        name_label.grid(row=0, column=0, padx=(15, 10), pady=5)

        name_input = ttk.Entry(sd_frame, width=20, textvariable=self.var_name, font=(
            "times new roman", 12, "bold"))
        name_input.grid(row=0, column=1, padx=10, pady=2, sticky=W)

        # roll no
        roll_label = Label(sd_frame, text="student no",
                           font=("times new roman", 12, "bold"))
        roll_label.grid(row=1, column=0, padx=(15, 10), pady=5)

        roll_input = ttk.Entry(sd_frame, width=20, textvariable=self.var_roll, font=(
            "times new roman", 12, "bold"))
        roll_input.grid(row=1, column=1, padx=10, pady=2, sticky=W)

        # division
        batch_label = Label(sd_frame, text="PRN",
                            font=("times new roman", 12, "bold"))
        batch_label.grid(row=2, column=0, padx=(15, 10), pady=5)

        batch_input = ttk.Entry(sd_frame, width=20, textvariable=self.var_batch, font=(
            "times new roman", 12, "bold"))
        batch_input.grid(row=2, column=1, padx=10, pady=2, sticky=W)

        # radio
        self.var_radio1 = tk.StringVar()
        radiobtn1 = ttk.Radiobutton(
            sd_frame,variable=self.var_radio1,  text="take photo sample", value="Yes")
        radiobtn1.grid(row=3, column=0, padx=20, pady=5)

        
        radiobtn2 = ttk.Radiobutton(
            sd_frame,variable=self.var_radio1, text="do not take photo", value="No")
        radiobtn2.grid(row=3, column=1, padx=10, pady=5)

        # buttonframe
        btn_frame = Frame(sd_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=165, width=580, height=70)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, font=(
            "times new roman", 12, "bold"), bg="indianred1", fg="white", width=15)
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="update",command=self.update_data, font=(
            "times new roman", 12, "bold"), bg="indianred1", fg="white", width=15)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="delete",command=self.delete_data, font=(
            "times new roman", 12, "bold"), bg="indianred1", fg="white", width=15)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="reset",command=self.reset_data, font=(
            "times new roman", 12, "bold"), bg="indianred1", fg="white", width=15)
        reset_btn.grid(row=0, column=3)

        pht_btn = Button(btn_frame, text="take photo",command=self.generate_dataset, font=(
            "times new roman", 12, "bold"), bg="turquoise3", fg="white", width=15)
        pht_btn.grid(row=1, column=1)
        upht_btn = Button(btn_frame, text="update photo", font=(
            "times new roman", 12, "bold"), bg="turquoise3", fg="white", width=15)
        upht_btn.grid(row=1, column=2)

        # right label
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details2", font=("times new roman", 12, "bold"))
        Right_frame.place(x=650, y=10, width=590, height=420)

        # search frame
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="search student", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=10, width=570, height=60)

        search_label = Label(search_frame, text="Search by",
                             font=("times new roman", 12, "bold"))
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12, "bold"), width=10, state="readonly")
        search_combo["values"] = ("choose", "Roll no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=2, sticky=W)

        search_input = ttk.Entry(
            search_frame, width=20, font=("times new roman", 12, "bold"))
        search_input.grid(row=0, column=2, padx=10, pady=2, sticky=W)

        # button
        search_btn = Button(search_frame, text="search", font=(
            "times new roman", 12, "bold"), bg="indianred1", fg="white", width=5)
        search_btn.grid(row=0, column=3, padx=10, pady=2)

        showall_btn = Button(search_frame, text="Show all", font=(
            "times new roman", 12, "bold"), bg="indianred1", fg="white", width=5)
        showall_btn.grid(row=0, column=4, padx=10, pady=2)

        # table frame
        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                 text="result", font=("times new roman", 12, "bold"))
        table_frame.place(x=10, y=80, width=550, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            "dep", "year", "sem", "roll", "name","batch", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("roll", text="Student no")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("batch", text="PRN")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("batch", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if (
           self.var_dep.get() == "select" or
           self.var_year.get() == "select year" or
           self.var_sem.get() == "select semester" or
           self.var_name.get() == "" or
           self.var_roll.get() == ""
           ):
            messagebox.showerror(
                "Error", "Please fill in all fields.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student1 values(%s,%s,%s,%s,%s,%s,%s)", (self.var_dep.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_batch.get(),
                                                                                        self.var_radio1.get(),
                                                                                        
                                                                                        
                                                                                        )
                                  )

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", "student details added")
            except Exception as es:
                messagebox.showerror(
                    "error", f"Due to :{str(es)}", parent=self.root)
                
                
    #fetch
    def fetch_data(self):
        conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student1")
        data=my_cursor.fetchall()
         
        if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
        conn.close()
        
        
    #function
    def get_cursor(self,event=""):
        
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
            
        self.var_dep.set(data[0])
        self.var_year.set(data[1])
        self.var_sem.set(data[2])
        self.var_roll.set(data[3])
        self.var_name.set(data[4])
        self.var_batch.set(data[5])
        self.var_radio1.set(data[6])
   
   
    #update
    def update_data(self):
        if (
           self.var_dep.get() == "select" or
           self.var_year.get() == "select year" or
           self.var_sem.get() == "select semester" or
           self.var_name.get() == "" or
           self.var_roll.get() == ""
           ):
            messagebox.showerror(
                "Error", "Please fill in all fields.", parent=self.root)
        else:
            try:
                updata=messagebox.askyesno("update","do you want to update the data",parent=self.root)
                if updata>0:
                    conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognition")
                    my_cursor = conn.cursor()
                    
                    
                    my_cursor.execute("UPDATE student1 SET department=%s,year=%s,semester=%s,name=%s,batch=%s,photosample=%s WHERE roll_no=%s",
                                                                                      ( self.var_dep.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_sem.get(),
                                                                                         
                                                                                        self.var_name.get(),
                                                                                        self.var_batch.get(),
                                                                                        self.var_radio1.get(),
                                                                                        self.var_roll.get()
                                                                                       )
                                                                                         
                                     )
                    
                
                
                
                else:
                    if not updata:
                        return
                    
                messagebox.showinfo("success","data updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                
            except Exception as es:
             messagebox.showerror("error",f"due to :{str(es)}",parent=self.root)
            
        
        
    #delete function
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("error","fill roll no",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete the student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql="delete from student1 where roll_no=%s"
                    val=(self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","successfully deleted detail",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)
                
                
    #resetn data 
    def reset_data(self):
        self.var_dep.set("select") 
        self.var_year.set("select year")
        self.var_sem.set("select semester")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_batch.set("")
        self.var_radio1.set("")
            
    #genereate dataset
    def generate_dataset(self):
        if (
           self.var_dep.get() == "select" or
           self.var_year.get() == "select year" or
           self.var_sem.get() == "select semester" or
           self.var_name.get() == "" or
           self.var_roll.get() == ""
           ):
            messagebox.showerror(
                "Error", "Please fill in all fields.", parent=self.root)
        else:
            try:   
                    roll = self.var_roll.get()
                    if roll.isdigit():
                      roll = int(roll)
                    else:
                       messagebox.showerror("Error", "Roll number should be a valid integer.", parent=self.root)
                       return
                
                    conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from student1")
                    myresult=my_cursor.fetchall()
                    id=0 
                    for x in myresult:
                        id+=1
                    my_cursor.execute("UPDATE student1 SET department=%s,year=%s,semester=%s,name=%s,batch=%s,photosample=%s WHERE roll_no=%s",
                                                                                      ( self.var_dep.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_sem.get(),
                                                                                         
                                                                                        self.var_name.get(),
                                                                                        self.var_batch.get(),
                                                                                        self.var_radio1.get(),
                                                                                        int(self.var_roll.get())==id+1
                                                                                       )
                                                                                         
                                     )
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)

                        for(x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                    cap=cv2.VideoCapture(0)
                    
                    img_id=0
                    
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpeg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255, 0), 2)

                            cv2.imshow("cropped face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("result","completing generating dataset")
            except Exception as es:
                 messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)

        
            
            
            
    
        
                    
            
        
        


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
