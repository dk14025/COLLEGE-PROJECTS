from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import PIL
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1530x790+0+0")
        self.root.geometry("1280x650+0+0")
        self.root.title("Face recognition Attendance System")

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

        title_lbl = Label(bg_img, text="Face Recognition", font=(
            "lucida sans typewriter", 35, "bold"), bg="darkseagreen1", fg="violetred1")
        title_lbl.place(x=0, y=0, width=1280, height=45)



        #button
        img9 = Image.open(r"images\ffrr.png")
        img9 = img9.resize((160, 160), PIL.Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
      
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=520,y=150,width=160,height=160)
       
        b1_1=Button(bg_img,text="face recognizer",cursor="hand2",font=("lucida sans typewriter",10,"bold"),bg="darkseagreen1",fg="red",command=self.facer)
        b1_1.place(x=520,y=310,width=160,height=30)
    

    #mark attendance
    def mark_attendance(self,r,n,d):
        with open("attfile.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((r not in name_list) and (n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{dtString},{d1},Present")



     #face recognixer
    def facer(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                

                confidence=int((100*(1-predict/300)))
                            
                conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="face_recognition")
                my_cursor = conn.cursor()  

                
               

                # my_cursor.execute("select roll_no from student1 where roll_no="+str(1))
                # roll= my_cursor.fetchone() 
                # roll = "+".join(roll)

                # my_cursor.execute("select name from student1 where roll_no="+str(1))
                # name= my_cursor.fetchone()
                # name = "+".join(name)
              
                # my_cursor.execute("select department from student1 where roll_no="+str(1))
                # dep = my_cursor.fetchone() 
                # dep = "+".join(dep)

                # my_cursor.execute("select roll_no from student1 where roll_no=" + str(id))
                # roll = my_cursor.fetchone()
#********************************************************************************************
                # my_cursor.execute("select roll_no from student1 where roll_no=" + str(10))
                # r = my_cursor.fetchone()
                # r = "+".join(r) if r is not None else "Unknown"

                # my_cursor.execute("select name from student1 where roll_no=" + str(10))
                # n = my_cursor.fetchone()
                # n = "+".join(n) if n is not None else "Unknown"

                # my_cursor.execute("select department from student1 where roll_no=" + str(10))
                # d = my_cursor.fetchone()
                # d = "+".join(d) if d is not None else "Unknown"
#***************************************************************************************************
                my_cursor.execute("select batch from student1 where roll_no="+str(id))
                r = my_cursor.fetchone()
                r = ", ".join(map(str, r)) if r is not None else "inaccesible"

                my_cursor.execute("select name from student1 where roll_no="+str(id))
                n = my_cursor.fetchone()
                n = ", ".join(map(str, n)) if n is not None else "inaccesible"
                my_cursor.execute("select department from student1 where roll_no="+str(id))
                d = my_cursor.fetchone()
                d = ", ".join(map(str, d)) if d is not None else "inaccesible"


                 




                # if roll is not None:
                #     roll = "+".join(roll)
                # else:
                #     roll = "Unknown"  # Set a default value for unknown faces

                # Similarly, handle name and department in a similar way
                # my_cursor.execute("select name from student1 where roll_no=" + str(id))
                # name = my_cursor.fetchone()
                # if name is not None:
                #     name = "+".join(name)
                # else:
                #     name = "Unknown"

                # my_cursor.execute("select department from student1 where roll_no=" + str(id))
                # dep = my_cursor.fetchone()
                # if dep is not None:
                #     dep = "+".join(dep)
                # else:
                #     dep = "Unknown"


               


                if confidence>76:
                    
                    cv2.putText(img, f"PRN:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),1)
                    cv2.putText(img,f"dep:{d}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),1)
                    self.mark_attendance(r,n,d)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"unknown",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),1)
            
                coord=[x,y,w,h]
            return coord
    
        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
    
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("welcome to face recognition", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_cap.release()
        cv2.destroyAllWindows()
        self.root.quit()  # Close the Tkinter window


        # faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # clf=cv2.face.LBPHFaceRecognizer_create()
        # clf.read("classifier.xml")

        # video_cap=cv2.VideoCapture(0)

        # while True:
        #     ret,img=video_cap.read()
        #     img=recognize(img,clf,faceCascade)
        #     cv2.imshow("welcome to face recognition",img)

        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break
        # video_cap.release()
        # cv2.destroyAllWindows()
               
    


if __name__ == "__main__":
    root = Tk()
    obj = Face(root)
    root.mainloop()

