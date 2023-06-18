# import required modules
import cv2
import numpy as np
import pandas as pd
import argparse
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
# contrast border thumbnail 
root = Tk()
root.title("Simple Photo Editor")
root.geometry("640x640")
# create functions
def selected():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd()) 
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    imgg = img.filter(ImageFilter.BoxBlur(0))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image=img1
    
def blur(event):
    global img_path, img1, imgg
    for m in range(0, v1.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = img.filter(ImageFilter.BoxBlur(m))
            img1 = ImageTk.PhotoImage(imgg) 
            canvas2.create_image(300, 210, image=img1)
            canvas2.image=img1
def brightness(event):
    global img_path, img2, img3
    for m in range(0, v2.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Brightness(img)
            img2 = imgg.enhance(m)
            img3 = ImageTk.PhotoImage(img2)
            canvas2.create_image(300, 210, image=img3)
            canvas2.image=img3
def contrast(event):
    global img_path, img4, img5
    for m in range(0, v3.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Contrast(img)
            img4 = imgg.enhance(m)
            img5 = ImageTk.PhotoImage(img4)
            canvas2.create_image(300, 210, image=img5)
            canvas2.image=img5
def rotate_image(event):
        global img_path, img6, img7
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img6 = img.rotate(int(rotate_combo.get()))
        img7 = ImageTk.PhotoImage(img6)
        canvas2.create_image(300, 210, image=img7)
        canvas2.image=img7
        
def flip_image(event):
        global img_path, img8, img9
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        if flip_combo.get() == "FLIP LEFT TO RIGHT":
            img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif flip_combo.get() == "FLIP TOP TO BOTTOM":
            img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
        img9 = ImageTk.PhotoImage(img8)
        canvas2.create_image(300, 210, image=img9)
        canvas2.image=img9   
def image_border(event):
    global img_path, img10, img11
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img10 = ImageOps.expand(img, border=int(border_combo.get()), fill=95)
    img11 = ImageTk.PhotoImage(img10)
    canvas2.create_image(300, 210, image=img11)
    canvas2.image=img11    
img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None
def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    #file=None
    ext = img_path.split(".")[-1]
    file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
    if file: 
            if canvas2.image==img1:
                imgg.save(file)
            elif canvas2.image==img3:
                img2.save(file)
            elif canvas2.image==img5:
                img4.save(file)
            elif canvas2.image==img7:
                img6.save(file)
            elif canvas2.image==img9:
                img8.save(file)
            elif canvas2.image==img11:
                img10.save(file)        
# create labels, scales and comboboxes
blurr = Label(root, text="Blur:", font=("ariel 17 bold"), width=9, anchor='e')
blurr.place(x=15, y=8)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur) 
scale1.place(x=150, y=10)
bright = Label(root, text="Brightness:", font=("ariel 17 bold"))
bright.place(x=8, y=50)
v2 = IntVar()   
scale2 = ttk.Scale(root, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness) 
scale2.place(x=150, y=55)
contrast = Label(root, text="Contrast:", font=("ariel 17 bold"))
contrast.place(x=35, y=92)
v3 = IntVar()   
scale3 = ttk.Scale(root, from_=0, to=10, variable=v3, orient=HORIZONTAL, command=contrast) 
scale3.place(x=150, y=100)
rotate = Label(root, text="Rotate:", font=("ariel 17 bold"))
rotate.place(x=370, y=8)
values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(root, values=values, font=('ariel 10 bold'))
rotate_combo.place(x=460, y=15)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)
flip = Label(root, text="Flip:", font=("ariel 17 bold"))
flip.place(x=400, y=50)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
flip_combo = ttk.Combobox(root, values=values1, font=('ariel 10 bold'))
flip_combo.place(x=460, y=57)
flip_combo.bind("<<ComboboxSelected>>", flip_image)
border = Label(root, text="Add border:", font=("ariel 17 bold"))
border.place(x=320, y=92)
values2 = [i for i in range(10, 45, 5)]
border_combo = ttk.Combobox(root, values=values2, font=("ariel 10 bold"))
border_combo.place(x=460, y=99)
border_combo.bind("<<ComboboxSelected>>", image_border)
# create canvas to display image
canvas2 = Canvas(root, width="600", height="420", relief=RIDGE, bd=2)
canvas2.place(x=15, y=150)
# create buttons
btn1 = Button(root, text="Select Image", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=selected)
btn1.place(x=100, y=595)
btn2 = Button(root, text="Save", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=save)
btn2.place(x=280, y=595)
btn3 = Button(root, text="Exit", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
btn3.place(x=460, y=595)

#Creating argument parser to take image path from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

#Reading the image with opencv
img = cv2.imread(img_path)

#declaring global variables (are used later on)
clicked = False
r = g = b = xpos = ypos = 0

#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

#function to calculate minimum distance from all colors and get the most matching color
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

#function to get x,y coordinates of mouse double click
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while(1):

    cv2.imshow("image",img)
    if (clicked):
   
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()
root.mainloop()