from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import PIL
from student import Attendance
import os
from train import Train
from face_recog import Face
from attendance import Att



class Face_Recongnition_System:
    def __init__(self,root ):
        self.root=root 
        #self.root.geometry("1530x790+0+0")
        self.root.geometry("1280x650+0+0")
        self.root.title("Face recognition Attendance System")


        #banner (only 1)
        img2 = Image.open(r"C:\Users\Deb Pattanayak\OneDrive\Desktop\face_recog_attendance\images\bannerf.jpg")
        img2 = img2.resize((1280, 120), PIL.Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0, y=0, width=1280, height=120)




        # #banner1
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

        #background
        img4 = Image.open(r"images\bg2.jpg")
        img4 = img4.resize((1280, 550), PIL.Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1280, height=550)

        title_lbl=Label(bg_img,text="FACE  RECOGNIZATION  ATTENDANCE  SYSTEM",font=("lucida sans typewriter",35,"bold"),bg="darkseagreen1",fg="violetred1")
        title_lbl.place(x=0,y=0,width=1280,height=45)
  

       #button1
        img5 = Image.open(r"images\button1.png")
        img5 = img5.resize((160, 160), PIL.Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
       
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.student_d)
        b1.place(x=120,y=150,width=160,height=160)
       
        b1_1=Button(bg_img,text="data",cursor="hand2",font=("lucida sans typewriter",10,"bold"),bg="darkseagreen1",fg="red",command=self.student_d)
        b1_1.place(x=120,y=310,width=160,height=30)

        #button2
        img6 = Image.open(r"images\button2.png")
        img6 = img6.resize((160, 160), PIL.Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
       
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=320,y=150,width=160,height=160)
       
        b1_1=Button(bg_img,text="face recognizer",command=self.face_data,cursor="hand2",font=("lucida sans typewriter",10,"bold"),bg="darkseagreen1",fg="red")
        b1_1.place(x=320,y=310,width=160,height=30)

        #button3
        img7 = Image.open(r"images\button3.png")
        img7 = img7.resize((160, 160), PIL.Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
       
        b1=Button(bg_img,image=self.photoimg7,command=self.attendance_data,cursor="hand2")
        b1.place(x=520,y=150,width=160,height=160)
       
        b1_1=Button(bg_img,text="attandance",cursor="hand2",command=self.attendance_data,font=("lucida sans typewriter",10,"bold"),bg="darkseagreen1",fg="red")
        b1_1.place(x=520,y=310,width=160,height=30)

        #button4
        img9 = Image.open(r"C:\Users\Deb Pattanayak\OneDrive\Desktop\face_recog_attendance\images\button4.png")
        img9 = img9.resize((160, 160), PIL.Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
       
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=720,y=150,width=160,height=160)
       
        b1_1=Button(bg_img,text="train data",cursor="hand2",font=("lucida sans typewriter",10,"bold"),bg="darkseagreen1",fg="red",command=self.train_data)
        b1_1.place(x=720,y=310,width=160,height=30)

        #button5
        img10 = Image.open(r"C:\Users\Deb Pattanayak\OneDrive\Desktop\face_recog_attendance\images\button5.png")
        img10 = img10.resize((160, 160), PIL.Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
       
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_image)
        b1.place(x=920,y=150,width=160,height=160)
       
        b1_1=Button(bg_img,text="stored data",command=self.open_image,cursor="hand2",font=("lucida sans typewriter",10,"bold"),bg="darkseagreen1",fg="red")
        b1_1.place(x=920,y=310,width=160,height=30)


         #exit button
        b3_1=Button(bg_img,text="exit",cursor="hand2",command=self.exitf,font=("lucida sans typewriter",10,"bold"),bg="red",fg="white")
        b3_1.place(x=1100,y=470,width=160,height=30)

    
   # open image
    def open_image(self):
        os.startfile("data")


    def student_d(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Att(self.new_window)
    
    def exitf(self):
        self.exitf=messagebox.askyesno("FRAS","you want to exit?",parent=self.root)
        if self.exitf>0:
            self.root.destroy()
        else:
            return
        
    



        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recongnition_System(root)
    root.mainloop()
