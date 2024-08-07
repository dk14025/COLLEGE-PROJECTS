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


class Train:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1530x790+0+0")
        self.root.geometry("1280x650+0+0")
        self.root.title("Face recognition Attendance System")

    #banner
        img2 = Image.open(
            r"images\bannerf.jpg")
        img2 = img2.resize((1280, 120), PIL.Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=0, y=0, width=1280, height=120)
        #background
        img4 = Image.open(
            r"images\bg2.jpg")
        img4 = img4.resize((1280, 550), PIL.Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1280, height=550)

        title_lbl = Label(bg_img, text="Train data", font=(
            "lucida sans typewriter", 35, "bold"), bg="darkseagreen1", fg="violetred1")
        title_lbl.place(x=0, y=0, width=1280, height=45)
          #button
        img9 = Image.open(r"images\trainbb.png")
        img9 = img9.resize((160, 160), PIL.Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
      
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_classifier)
        b1.place(x=520,y=150,width=160,height=160)
       
        b1_1=Button(bg_img,text="train data",cursor="hand2",font=("lucida sans typewriter",10,"bold"),bg="darkseagreen1",fg="red",command=self.train_classifier)
        b1_1.place(x=520,y=310,width=160,height=30)
    
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        clf = cv2.face.LBPHFaceRecognizer_create()


        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","training dataset completed")




if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
