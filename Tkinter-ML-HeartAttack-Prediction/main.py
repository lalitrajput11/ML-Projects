from tkinter import *
from datetime import date
from tkinter import messagebox
from tkinter.ttk import Combobox

from mpl_toolkits.mplot3d import Axes3D
import datetime
import tkinter as ttk
import tkinter as tk

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np



import sys
import os


background = '#f0ddd5'
framebg ='#62a7ff'
framefg='#fefbfb'

root=Tk()
root.title('Heart Attack Prediction System')
root.geometry("1450x730+60+80")
root.resizable(False,False)
root.config(bg=background)

        
    

## Analysis <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def analysis():
    name=Name.get()
    D1=Date.get()
    today=datetime.date.today()
    A= today.year-DOB.get()
    
    try:
        B=selection()
    except:
        messagebox.showerror('Missing!, Please Select Gender')
        return
    
    try:
        F=selection1()
    except:
        messagebox.showerror('Missing!, Please Select fbs')
        return
    
    try:
        I=selection2()
    except:
        messagebox.showerror('Missing!, Please Select Exang')
        return
    
    try:
        C = int(selection3())
    except TypeError:
        messagebox.showerror('Missing!, Please Select cp')
        return
  
    try:
        G=int(restceg_combobox.get())
    except:
        messagebox.showerror('Missing!, Please Select restceg')
        return
    
    try:
        K=int(selection4())
    except TypeError:  # catch TypeError instead of general exception
        messagebox.showerror('Missing!, Please Select Slope')
        return
    
    try:
        L=int(ca_combobox.get())
    except:
        messagebox.showerror('Missing!, Please Select Ca')
        return
    
    try:
        M=int(thal_combobox.get())
    except:
        messagebox.showerror('Missing!, Please Select thal')
        return
    
    try: 
        D=int(Trestbps.get())
        E=int(chol.get())
        H=int(thalach.get())
        J=int(oldpeak.get())
    except:
        messagebox.showerror('Missing Data!!, Few Missing Data Entry')
        return
        
        #lets check all are working or not : 
        
    print('A is age:',A)
    print('B is gender:',B)
    print('C is cp:',C)        
    print('D is trestbps :',D)
    print('E is chol :',E)
    print('F is fbs:',F)
    print('G is restcg:',G)
    print('H is thalach:',H)
    print('I is Exang:',I)
    print('J is oldpeak:',J)
    print('K is slop:',K)
    print('L is ca:',L)
    print('M is thal:',M)   
        
        
    ###First Graph <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    f= Figure(figsize=(5,5),dpi=100)
    a = f.add_subplot(111)
    a.plot(['Sex','fbs','exang'],[B, F, I])
    canvas = FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=TRUE)
    canvas._tkcanvas.place(width=250,height=250,x=600,y=240)
    
    ###Secondt Graph <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    f2= Figure(figsize=(5,5),dpi=100)
    a = f2.add_subplot(111)
    a.plot(['age','trestbps','chol','thalach'],[A, D, E, H])
    canvas = FigureCanvasTkAgg(f2)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=TRUE)
    canvas._tkcanvas.place(width=250,height=250,x=864,y=240)
    
###Third Graph <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    f3= Figure(figsize=(5,5),dpi=100)
    a = f3.add_subplot(111)
    a.plot(['oldpeak','resticg','CP'],[J,G,C])
    canvas = FigureCanvasTkAgg(f3)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=TRUE)
    canvas._tkcanvas.place(width=250,height=250,x=600,y=470)
    
###Fourth Graph <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    f4= Figure(figsize=(5,5),dpi=100)
    a = f4.add_subplot(111)
    a.plot(['slope','ca','thal'],[K,L,M])
    canvas = FigureCanvasTkAgg(f4)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=TRUE)
    canvas._tkcanvas.place(width=250,height=250,x=864,y=470)
    
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<BackEnd<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score
    import backend
    
    
    heart_data = pd.read_csv('/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/heart.csv')
    
    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
    X.columns = [str(col) for col in X.columns]  # Reset column name
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)

    
        ## Input data
    input_data =(A,B,C,D,E,F,G,H,I,J,K,L,M)
    input_data_as_numpy_array=np.asanyarray(input_data)
    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)
    
    prediction =model.predict(input_data_reshape)
    
    print(prediction[0])
    
    if prediction[0]==0:
        print("The person dosen't have heart disease")
        report.config(text=f"Report:{0}",fg="#8dc63f")
        report1.config(text={f"{name}, you do not have a Heart Disease "})
    else:
        print("The person has heart disease")
        report.config(text=f"Report:{1}",fg="#ed1c24")
        report1.config(text={f"{name}, you have a Heart Disease "})
        
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<BackEnd
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    
## info window operated by info button
def info():
    Icon_window=Toplevel(root)
    Icon_window.title('Info')
    Icon_window.geometry("700x600+400+100")

    # icoon image
    icon_image = PhotoImage(file='/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/icon.png')
    Icon_window.iconphoto(False,icon_image)

    # Heading 
    Label(Icon_window,text='Information Related to dataset',font='robot 19 bold').pack(padx=20,pady=20)

    # info
    Label(Icon_window,text="age - age in years",font="arial 11").place(x=20,y=100)
    Label(Icon_window,text="sex - sex (1 = male; 0 = female)",font="arial 11").place(x=20,y=130)
    Label(Icon_window,text="cp - chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3 = asymptomatic)",font="arial 11").place(x=20,y=160)
    Label(Icon_window,text="trestbps - resting blood pressure (in mm Hg on admission to the hospital)",font="arial 11").place(x=20,y=190)
    Label(Icon_window,text="chol - serum cholestoral in mg/dl",font="arial 11").place(x=20,y=220)
    Label(Icon_window,text="fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)",font="arial 11").place(x=20,y=250)
    Label(Icon_window,text="restecg - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)",font="arial 11").place(x=20,y=280)
    Label(Icon_window,text="thalach - maximum heart rate achieved",font="arial 11").place(x=20,y=310)
    Label(Icon_window,text="exang - exercise induced angina (1 = yes; 0 = no)",font="arial 11").place(x=20,y=340)
    Label(Icon_window,text="oldpeak - ST depression induced by exercise relative to rest",font="arial 11").place(x=20,y=370)
    Label(Icon_window,text="slope - the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)",font="arial 11").place(x=20,y=400)
    Label(Icon_window,text="ca - number of major vessels (0-3) colored by flourosopy",font="arial 11").place(x=20,y=430)
    Label(Icon_window,text="thal - 0 = normal; 1 = fixed defect; 2 = reversable defect",font="arial 11").place(x=20,y=470)

    Icon_window.mainloop()

####################################

## For closing window
def logout():
    root.destroy()

####################################

## clear : with the help of clear , we can clear whole entry
def clear():
    Name.get('')
    DOB.get('')
    Trestbps.get('')
    chol.get("")
    thalach.get('')
    oldpeak.set('')
    
#icon1

image_icon = PhotoImage(file='/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/icon.png')
root.image_icon = image_icon  # keep a reference to the image


#header sction 2

logo = PhotoImage(file='/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/header.png')
myimage = Label(image=logo,bg=background)
myimage.place(x=0,y=0)

#header frame 3

Heading_entry= Frame(root,width=800,height=190,bg='#df2d4b')
Heading_entry.place(x=600,y=20)

Label(Heading_entry,text='Registration No.',font='arial 13',bg ='#df2d4b',fg =framefg).place(x=30,y=0)
Label(Heading_entry,text='Date',font='arial 13',bg ='#df2d4b',fg =framefg).place(x=430,y=0)


Label(Heading_entry,text='Patient Name',font='arial 13',bg ='#df2d4b',fg =framefg).place(x=30,y=90)
Label(Heading_entry,text='Birth Year',font='arial 13',bg ='#df2d4b',fg =framefg).place(x=430,y=90)

Entry_Image= PhotoImage(file='/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/Rounded Rectangle 1.png')
Entry_Image2 =PhotoImage(file="/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/Rounded Rectangle 2.png")

Label(Heading_entry,image=Entry_Image,bg='#df2d4b').place(x=20,y=30)
Label(Heading_entry,image=Entry_Image,bg='#df2d4b').place(x=430,y=30)

Label(Heading_entry,image=Entry_Image2,bg='#df2d4b').place(x=20,y=120)
Label(Heading_entry,image=Entry_Image2,bg='#df2d4b').place(x=430,y=120)

Registration = IntVar()
reg_entry = Entry(Heading_entry,textvariable=Registration,width=20,font="arail 15",bg='#0e5363',fg='white',bd=0)
reg_entry.place(x=20,y=45)

Date =StringVar()
today = date.today()
d1=today.strftime('%d/%m/%Y')
data_entry= Entry(Heading_entry, textvariable=Date,width =15,font='#0e5363',bg='#0e5363',fg='white',bd=0)
data_entry.place(x=500,y=45)
Date.set(d1)

Name =StringVar()
name_entry = Entry(Heading_entry,textvariable=Name,width=20,font="arail 15",bg='#0e5363',fg='white',bd=0)
name_entry.place(x=30,y=130)

DOB =IntVar()
dob_entry = Entry(Heading_entry,textvariable=DOB,width=20,font="arail 15",bg='#0e5363',fg='white',bd=0)
dob_entry.place(x=450,y=130)



#######################################BODY###############################################################

Detail_entry =Frame(root,width=525,height=260,bg='#dbe0e3')
Detail_entry.place(x=30,y=400)

# RadioButton

Label(Detail_entry,text='sex',font = 'arial 13',bg= framebg,fg = framefg).place(x=10,y=10)
Label(Detail_entry,text='fbs',font = 'arial 13',bg= framebg,fg = framefg).place(x=182,y=10)
Label(Detail_entry,text='exang',font = 'arial 13',bg= framebg,fg = framefg).place(x=335,y=10)


def selection():
    global gen  # declare Gender as a global variable
    if gen.get()==1:
        Gender = 1
    elif gen.get()==2:
        Gender = 0
    else:
        Gender = None  # assign a default value to Gender
    return Gender

def selection1():
    if fbs.get()==1:
        Fbs=1
        return Fbs
        
    elif fbs.get()==0:
        Fbs=0
        return Fbs
    
    else:
        return None
        
def selection2():
    if exang.get()==1:
        Exang=1
        return (Exang)
        
    elif exang.get()==0:
        Exang=0
        return (Exang)
    
    else:
        return None


gen=IntVar()
R1=Radiobutton(Detail_entry,text='Male',variable=gen,value=1,command=selection)
R2= Radiobutton(Detail_entry,text='Female',variable=gen,value=2,command=selection)

fbs=IntVar()
R3=Radiobutton(Detail_entry,text='True',variable=fbs,value=1,command= selection1)
R4= Radiobutton(Detail_entry,text='False',variable=fbs,value=2,command=selection1)

exang=IntVar()
R5=Radiobutton(Detail_entry,text='Yes',variable=exang,value=1,command=selection2)
R6= Radiobutton(Detail_entry,text='False',variable=exang,value=2,command=selection2)

R1.place(x=40,y=10)
R2.place(x=99,y=10)

R3.place(x=209,y=10)
R4.place(x=266,y=10)

R5.place(x=384,y=10)
R6.place(x=438,y=10)

#################################COMBOBOX#############################################################

Label(Detail_entry,text='cp :',font='arial 13',bg=framebg,fg=framefg).place(x=10,y=50)
Label(Detail_entry,text='restecg :',font='arial 13',bg=framebg,fg=framefg).place(x=10,y=90)
Label(Detail_entry,text='slope :',font='arial 13',bg=framebg,fg=framefg).place(x=10,y=130)
Label(Detail_entry,text='ca :',font='arial 13',bg=framebg,fg=framefg).place(x=10,y=170)
Label(Detail_entry,text='thal :',font='arial 13',bg=framebg,fg=framefg).place(x=10,y=210)

cp_combobox = Combobox(Detail_entry,values=['0=typical angina','1 = atypical angina','2= non-anginal pain','3=ayspmptomatic'],font ='arial 12',state='r',width=14)

restceg_combobox = Combobox(Detail_entry,values=['0','1','2'],font ='arial 12',state='r',width=11)
slope_combobox = Combobox(Detail_entry,values=['0=upsloping','1=flat','2=downsloping'],font ='arial 12',state='r',width=12)
ca_combobox = Combobox(Detail_entry,values=['0','1','2','3','4'],font ='arial 12',state='r',width=14)
thal_combobox = Combobox(Detail_entry,values=['0','1','2','3'],font ='arial 12',state='r',width=14)

cp_combobox.place(x=50,y=50)
restceg_combobox.place(x=80,y=90)
slope_combobox.place(x=70,y=130)
ca_combobox.place(x=50,y=170)
thal_combobox.place(x=50,y=210)

def selection3():
    input = cp_combobox.get()
    if input in ['0 =typical angina', '1 = atypical angina', '2= non-anginal pain', '3=ayspmptomatic']:
        if input == '0 =typical angina':
            return 0
        elif input == '1 = atypical angina':
            return 1
        elif input == '2= non-anginal pain':
            return 2
        elif input == '3=ayspmptomatic':
            return 3
    else:
        return None
    
def selection4():
    input=slope_combobox.get()
    if input== '0=upsloping':
        return 0
    elif input== '1=flat':
        return 1
    elif input== '2=downsloping':
        return 2
    else:
        return None  # return None instead of printing Exang

###############################DATA ENTRY BOX############################################################################

Label(Detail_entry,text='Smoking:',font='arail 13',width =7, bg=framebg,fg=framefg).place(x=240,y=50)
Label(Detail_entry,text='Trestbps:',font='arail 13',width =7, bg=framebg,fg=framefg).place(x=240,y=90)
Label(Detail_entry,text='Chol:',font='arail 13',width =7, bg=framebg,fg=framefg).place(x=240,y=130)
Label(Detail_entry,text='Thalach:',font='arail 13',width =7,bg=framebg,fg=framefg).place(x=240,y=170)
Label(Detail_entry,text='Oldpeak: ',font='arail 13',width =7, bg=framebg,fg=framefg).place(x=240,y=210)

Trestbps = StringVar()
chol = StringVar()
thalach = StringVar()
oldpeak = StringVar()

Trestbps_entry = Entry(Detail_entry,textvariable=Trestbps,width =10,font='arial 15',bg='#ededed',fg='#222222',bd=0)
chol_entry = Entry(Detail_entry,textvariable=chol,width =10,font='arial 15',bg='#ededed',fg='#222222',bd=0)
thalach_entry = Entry(Detail_entry,textvariable=thalach,width =10,font='arial 15',bg='#ededed',fg='#222222',bd=0)
oldpeak_entry = Entry(Detail_entry,textvariable=oldpeak,width =10,font='arial 13',bg='#ededed',fg='#222222',bd=0)

Trestbps_entry.place(x=330,y=90)
chol_entry.place(x=330,y=130)
thalach_entry.place(x=330,y=170)
oldpeak_entry.place(x=330,y=210)

############################################# REPORT #################################################################

square_report_image= PhotoImage(file ='/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/Report.png')
report_background = Label(image=square_report_image,bg =background)
report_background.place(x=1120,y=340)

report = Label(root,font=' arial 15 bold',bg='white',fg ='#8dc63f')
report.place(x=1170,y=550)

report1 = Label(root,font=' arial 15 bold',bg='white',fg ='#8dc63f')
report1.place(x=1130,y=610)


################################################ GRAPH ########################################################################

graph_image = PhotoImage(file ='/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/graph.png')

Label(image=graph_image).place(x=600,y=270)
Label(image=graph_image).place(x=860,y=270)
Label(image=graph_image).place(x=600,y=500)
Label(image=graph_image).place(x=860,y=500)

################################################# BUTTON #################################################################################


ANALYSIS_BUTTON = PhotoImage(file ='/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/Analysis.png')
Button(root,image=ANALYSIS_BUTTON,bd=0,bg=background,command=analysis).place(x=1130,y=240)


################################################# iNFO bUTTON #################################################################################

Info_BUTTON = PhotoImage(file ='/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/info.png')
Button(root,image=Info_BUTTON,bd=0,bg=background,cursor='hand2',command=info).place(x=10,y=240)


################################################# Save bUTTON #################################################################################

save_button = PhotoImage(file='/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/save.png')
Button(root,image=save_button,bd=0,bg=background,cursor='hand2').place(x=1370,y=250)



########################################## Smoking and Nin Smoking Button ###################################################################

button_mode = True
choice ='smoking'

def changemod():
    global button_mode
    global choice
    if button_mode:
        choice ='non_smoking'
        mode.config(image=non_smoking_icon,activebackground='white')
        button_mode = False
        return choice
    else: 
        choice ='smoking'
        mode.config(image=smoking_icon,activebackground='white')
        button_mode = True
        return choice

smoking_icon =PhotoImage(file ='/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/smoker.png')
non_smoking_icon = PhotoImage(file='/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/non-smoker.png')


mode= Button(root,image=smoking_icon,bg='#dbe0e3',bd=0,cursor='hand2',command=changemod)
mode.place(x=355,y=445)




########################################## LogOut Button ###################################################################

logout_icon = PhotoImage(file='/home/lalitrajput/Downloads/Duact/tkinterMLHeartattack/Images-20240711T132944Z-001/Images/logout.png')
log_out_buttton=Button(root,image=logout_icon,bg='#df2d4b',bd=0,cursor='hand2',command=logout)
log_out_buttton.place(x=1390,y=60)




root.mainloop()