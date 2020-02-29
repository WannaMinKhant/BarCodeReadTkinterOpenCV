"""
A basic video playing option for TKinter GUI windows using openCV
Author 	: Ajinkya Padwad
Date 	: November 2017

install openCV first : sudo apt-get install libopencv-dev python-opencv

"""

import mysql.connector as mariadb
from mysql.connector import errorcode
import cv2
import tkinter as tk
from tkinter import *
import tkinter.ttk
from tkinter.ttk import Frame
from PIL import Image, ImageTk
import time
import numpy as np
import pyzbar.pyzbar as pyzbar
import serial



precode = 0

white 		= "#ffffff"
lightBlue2 	= "#adc5ed"
font 		= "Constantia"
fontButtons = (font, 12)
maxWidth  	= 650
maxHeight 	= 480

ser = serial.Serial('/dev/ttyACM0',9600, timeout=.1)
time.sleep(1)
ser.write("0".encode())
time.sleep(1)

#Graphics window
mainWindow = tk.Tk()
mainWindow.configure(bg=lightBlue2)
mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))
mainWindow.resizable(1,1)

canvas = Canvas(mainWindow, width = 200, height = 200)  
# canvas.pack() 
# mainWindow.overrideredirect(1)

mainFrame = Frame(mainWindow)
mainFrame.place(x=20, y=20)                

#Capture video frames
lmain = tk.Label(mainFrame)
lmain.grid(row=0, column=0)




cap = cv2.VideoCapture(0)

Name = StringVar(mainWindow)
BC = StringVar(mainWindow)
Dept = StringVar(mainWindow)
Rank = StringVar(mainWindow)

count = 0
def checkedCode(code):
    name = 0
    bc = 0
    dept = 0
    rank = 0
    img = "gaung.jpg"
    global count
    
    try:
        connection = mariadb.connect(host='localhost',
                database='Bio', user='minkhant', password='root')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print ('Connected to MySQL Server version ', db_Info)

            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            mySql_insert_query = \
                """SELECT * FROM outpass WHERE barcode = %s"""

            cursor = connection.cursor()
            print(code)
            result = cursor.execute(mySql_insert_query,(code,))
            
            results = cursor.fetchall()
            count = 0
            for row in results:
                count += 1
                name = row[2]
                bc = row[1]
                dept = row[3]
                rank = row[4]
                imgpath = row[6]
            
            if count > 0:
                setValue(name, bc, dept, rank, imgpath)
            else:
                reset()
            sendSerial(count,code)
            print(count)
    except IOError as e:
        print(e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print ('MySQL connection is closed')


def setValue(name,bc,dept,rank,imgpath):
    Name.set(name)
    BC.set(bc)
    Dept.set(dept)
    Rank.set(rank)
    img = Image.open(imgpath)
    imgtk = ImageTk.PhotoImage(image=img)
    pp.imgtk = imgtk
    pp.configure(image=imgtk)

def reset():
    Name.set("")
    BC.set("")
    Dept.set("")
    Rank.set("")
    img = Image.open("gaung.jpg")
    imgtk = ImageTk.PhotoImage(image=img)
    pp.imgtk = imgtk
    pp.configure(image=imgtk)
    
def sendSerial(passed,bcode):

    print("serial")
    global precode
    if bcode == precode:
        return
    print("OlD Code      "  + bcode)
    precode = bcode
    
    if passed == 1:
       ser.write("1".encode())
    else:
       ser.write("0".encode())
    time.sleep(0.5)
    print(precode)

code = 0

def show_frame():

    global code
    code = 0
    barcode = 0
    (ret, frame) = cap.read()

    decodedObjects = pyzbar.decode(frame)

    for obj in decodedObjects:
        barcode = obj.data
        code = barcode.decode("utf-8")
        coded = code
        checkedCode(code)
        print (barcode.decode("utf-8"))
    

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image).resize((320, 240))
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
    


closeButton = Button(mainWindow, text = "CLOSE", font = fontButtons, bg = white, width = 20, height= 1)
closeButton.configure(command= lambda: mainWindow.destroy())              
closeButton.place(x=75,y=410)

img = Image.open("gaung.jpg")
imgtk = ImageTk.PhotoImage(image=img)

    
pp = Label(mainWindow, textvariable=Name, font= fontButtons, image=imgtk)
pp.place(x= 400,y=20)
lblname = Label(mainWindow, textvariable=Name, font= fontButtons, bg = white, width = 20, height = 2)
lblname.place(x= 400,y=250)
lblcode = Label(mainWindow, textvariable=BC, font= fontButtons, bg = white, width = 20, height = 2)
lblcode.place(x= 400,y=300)
lblrank = Label(mainWindow, textvariable=Rank, font= fontButtons, bg = white, width = 20, height = 2)
lblrank.place(x= 400,y=350)
lbldept = Label(mainWindow, textvariable=Dept, font= fontButtons, bg = white, width = 20, height = 2)
lbldept.place(x= 400,y=400)



    

# setbtn = Button(mainWindow, text = "change", font = fontButtons, bg = white, width = 20, height= 1)
# setbtn.configure(command= lambda: sendSerial(count,code))              
# setbtn.place(x=75,y=380)	

show_frame()  #Display
mainWindow.mainloop()  #Starts GUI
ser.close()



