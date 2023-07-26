from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
from tkinter import messagebox
from time import strftime
from datetime import datetime


class FaceRecognition:
    def __init__(self, root):

    # =================face recognition==================
    def face_recog(self):
    def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            n = "Unknown"  # Set a default value for 'n'

        for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])

                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(username='root', password='root', host='localhost',database='face_recognition', port=3306)
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_ID=" + str(id))
                name_result = cursor.fetchone()
                if name_result:
                    n = name_result[0]  # Update 'n' with the fetched value from the database

                # ... (rest of the code) ...

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()

        # After the video capture loop ends, print the student information from the database
        conn = mysql.connector.connect(username='root', password='root', host='localhost',
                                       database='face_recognition', port=3306)
        cursor = conn.cursor()

        for (x, y, w, h) in features:
            gray_face = gray_image[y:y + h, x:x + w]
            id, predict = clf.predict(gray_face)
            if confidence < 50:
                print("Unknown student!")
            else:
                cursor.execute("SELECT Student_ID, Name, Roll_No FROM student WHERE Student_ID=" + str(id))
                student_info = cursor.fetchone()
                if student_info:
                    id, name, roll_no = student_info
                    print("Student ID:", id)
                    print("Name:", name)
                    print("Roll Number:", roll_no)
                else:
                    print("Unknown student!")

        cursor.close()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
