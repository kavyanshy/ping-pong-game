import turtle
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from tkinter import *
import datetime
from tkinter import messagebox

first = 0
second = 0

import mysql.connector
localhost= ""
user= ""
password=""

try:
    file2 = open("keys.txt","x")
    file2.close()
except:
    pass


file1 = open("keys.txt","r")
lines3 = file1.readlines()
lines = lines3[0].split(",")
print(lines)
file1.close()
localhost = lines[0]
user = lines[1]
zzz = lines[2].split("-")
password = zzz[0]
print(password)



config =  Tk()
ft2= tkFont.Font(family='Times',size=20)
ft3= tkFont.Font(family='Times',size=15)

localhostvar = StringVar(config)
localhostvar.set(localhost)

uservar = StringVar(config)
uservar.set(user)

passwordvar = StringVar(config)
passwordvar.set(password)

def Save_c(event):
    localhost = localhostvar.get()
    password = passwordvar.get()
    user  = uservar.get()

    file3 = open("keys.txt","w")
    file3.write(localhost+","+user+","+password+"-")
    file3.close()
    try:
        mydb5 = mysql.connector.connect(
            host=localhost,
            user=user,
            password=password
    )
        config.destroy()
    except:
        messagebox.showerror("Enter", "CAN'T CONNECT TO MYSQL CHECK CREDENTIALS AGAIN")
    

def setl(event):
    localhostvar.set(event.widget.get())

def setu(event):
    uservar.set(event.widget.get())

def setp(event):
    passwordvar.set(event.widget.get())

config.config(bg="#202124")

l_user6 =  Label(config,text="MYSQL CREDENTIALS",bg="#202124",fg="#877f86",font=ft2)
l_user6.pack(side= TOP)

l_user3 =  Label(config,text="host",bg="#202124",fg="#877f86",font=ft3)
l_user3.pack(side= TOP)

pas3 =  Entry(config,name="host",width=40,textvar=localhostvar)
pas3.pack()
pas3.bind("<Leave>",setl)


l_user4 =  Label(config,text="user",bg="#202124",fg="#877f86",font=ft3)
l_user4.pack(side= TOP)

pas4 =  Entry(config,name="user",width=40,textvar=uservar)
pas4.pack()
pas4.bind("<Leave>",setu)

l_user5 =  Label(config,text="password",bg="#202124",fg="#877f86",font=ft3)
l_user5.pack(side= TOP)

pas5 =  Entry(config,name="password",width=40,textvar=passwordvar)
pas5.pack()
pas5.bind("<Leave>",setp)

btn4 =  Button(config,text="SAVE",name="save")
btn4.pack()
btn4.bind("<Button-1>",Save_c)

config.mainloop()
mydb = mysql.connector.connect(
  host=localhost,
  user=user,
  password="pokemonz1$"
)

l = []
cursor  = mydb.cursor() 

cursor.execute("SHOW DATABASES")
for i in cursor:
    l.append(i)
    

try:
    if "ping_data1" not in l:
        cursor.execute("CREATE DATABASE PING_DATA1")
except:
    pass


def login(myPlayer):
  mydb2 = mysql.connector.connect(
  host=localhost,
  user=user,
  password="pokemonz1$",
  database="ping_data1"

)
  j = []

  cursor2 = mydb2.cursor()

  cursor2.execute("SHOW TABLES")
  for i in cursor2:
   j.append(i)
  """
  if myPlayer not in j:
        
   cursor2.execute("CREATE TABLE players (user VARCHAR(255), password VARCHAR(255), topscore VARCHAR(255),createON VARCHAR(255))")
   cursor2.execute("CREATE TABLE "+myPlayer+"(player1 VARCHAR(255), player2 VARCHAR(255), playedon VARCHAR(255))")
    """

  cursor2.execute("SELECT * FROM players WHERE user ="+myPlayer)
  results  = cursor2.fetchall()
  c =[]
  for i in results:
    c = list(i)
    c.append(c)
    return c[0],c[1]

def Register(myPlayer,password):
  mydb2 = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pokemonz1$",
  database="ping_data1"
)
  j = []

  cursor3 = mydb2.cursor()


  sql = "INSERT INTO players (user, password,topscore,createON) VALUES (%s, %s,%s,%s)"
  val = (myPlayer, password,"0",datetime.datetime.now())
  cursor3.execute(sql,val)
  mydb2.commit()  



def Pong():
    sc = turtle.Screen()
    sc.title("Pong game")
    sc.bgcolor("black")
    sc.setup(width=1000, height=600)
     
     
    # Left paddle
    left_pad = turtle.Turtle()
    left_pad.speed(0)
    left_pad.shape("square")
    left_pad.color("red")
    left_pad.shapesize(stretch_wid=6, stretch_len=2)
    left_pad.penup()
    left_pad.goto(-400, 0)
     
     
    # Right paddle
    right_pad = turtle.Turtle()
    right_pad.speed(0)
    right_pad.shape("square")
    right_pad.color("blue")
    right_pad.shapesize(stretch_wid=6, stretch_len=2)
    right_pad.penup()
    right_pad.goto(400, 0)
     
     
    # Ball of circle shape
    hit_ball = turtle.Turtle()
    hit_ball.speed(40)
    hit_ball.shape("circle")
    hit_ball.color("blue")
    hit_ball.penup()
    hit_ball.goto(0, 0)
    hit_ball.dx = 5
    hit_ball.dy = -5
     
     
    # Initialize the score
    left_player = 0
    right_player = 0
     
     
    # Displays the score
    sketch = turtle.Turtle()
    sketch.speed(0)
    sketch.color("blue")
    sketch.penup()
    sketch.hideturtle()
    sketch.goto(0, 260)
    sketch.write("Left_player : 0    Right_player: 0",
                 align="center", font=("Courier", 24, "normal"))
     
     
    # Functions to move paddle vertically
    def paddleaup():
        y = left_pad.ycor()
        y += 20
        left_pad.sety(y)
     
     
    def paddleadown():
        y = left_pad.ycor()
        y -= 20
        left_pad.sety(y)
     
     
    def paddlebup():
        y = right_pad.ycor()
        y += 20
        right_pad.sety(y)
     
     
    def paddlebdown():
        y = right_pad.ycor()
        y -= 20
        right_pad.sety(y)
     
     
    # Keyboard bindings
    sc.listen()
    sc.onkeypress(paddleaup, "e")
    sc.onkeypress(paddleadown, "x")
    sc.onkeypress(paddlebup, "Up")
    sc.onkeypress(paddlebdown, "Down")
     
     
    while True:
        sc.update()
     
        hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
        hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
     
        # Checking borders
        if hit_ball.ycor() > 280:
            hit_ball.sety(280)
            hit_ball.dy *= -1
     
        if hit_ball.ycor() < -280:
            hit_ball.sety(-280)
            hit_ball.dy *= -1
     
        if hit_ball.xcor() > 500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            left_player += 1
            sketch.clear()
            sketch.write("Left_player : {}    Right_player: {}".format(
                          left_player, right_player), align="center",
                          font=("Courier", 24, "normal"))
     
        if hit_ball.xcor() < -500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            right_player += 1
            sketch.clear()
            sketch.write("Left_player : {}    Right_player: {}".format(
                                     left_player, right_player), align="center",
                                     font=("Courier", 24, "normal"))
     
        # Paddle ball collision
        if (hit_ball.xcor() > 360 and
                            hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+40 and
                            hit_ball.ycor() > right_pad.ycor()-40):
            hit_ball.setx(360)
            hit_ball.dx*=-1

        if (hit_ball.xcor()<-360 and
                       hit_ball.xcor()>-370) and(hit_ball.ycor()<left_pad.ycor()+40 and
                        hit_ball.ycor()>left_pad.ycor()-40):
            hit_ball.setx(-360)
            hit_ball.dx*=-1
def Sign_up():
    

    window = Tk()

    setu1 = StringVar(window)
    setu1.set("u ")

    setp1 = StringVar(window)
    setp1.set("p")


    def btn_clicked():
        print(setu1.get(),setp1.get())
        Register(setu1.get(),setp1.get())
        window.destroy()
        Pong()

    def setuu(event):
        setu1.set(event.widget.get())

    def setpp(event):
        print("hii")
        setp1.set(event.widget.get())


    window.geometry("782x520")
    window.configure(bg = "#ec1616")
    canvas = Canvas(
        window,
        bg = "#ec1616",
        height = 520,
        width = 782,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(
        391.0, 260.0,
        image=background_img)

    canvas.create_text(
        115.5, 63.5,
        text = "Sign up",
        fill = "#000000",
        font = ("None", int(40.0)))

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        204.0, 191.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#dcd4d4",
        highlightthickness = 0)

    entry0.bind("<Leave>",setuu)

    entry0.place(
        x = 51.0, y = 166,
        width = 306.0,
        height = 48)

    entry1_img = PhotoImage(file = f"img_textBox1.png")
    entry1_bg = canvas.create_image(
        204.0, 293.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#dcd4d4",
        highlightthickness = 0)
    entry1.bind("<Leave>",setpp)
    entry1.place(
        x = 51.0, y = 268,
        width = 306.0,
        height = 48)

    canvas.create_text(
        96.5, 151.5,
        text = "username:",
        fill = "#000000",
        font = ("None", int(24.0)))

    canvas.create_text(
        97.5, 253.5,
        text = "password:",
        fill = "#000000",
        font = ("None", int(24.0)))

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 57, y = 401,
        width = 293,
        height = 46)

    window.resizable(False, False)
    window.mainloop()


def login1():
    login_wn =  Tk()
    strvar = StringVar(login_wn)
    strvar.set("password")

    uservar = StringVar(login_wn)
    uservar.set("peter")

    def run(event):
        key = login(strvar.get())
        print("user"+uservar.get(),"password"+ strvar.get())
        print(key)
        if key[0] == strvar.get():
            if key[1]==uservar.get():
                print("correct credentials")
                Pong()



    def passw(event):
        print(event.widget.get())
        strvar.set(event.widget.get())

    def usern(event):
        uservar.set(event.widget.get())
        print(strvar.get())



    login_wn.geometry("500x200")
    """
    login_wn.overrideredirect(True) # turns off title bar, geometry
    login_wn.geometry('400x100+200+200') # set new geometry

    # make a frame for the title bar
    title_bar = Frame(login_wn, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)

    # put a close button on the title bar
    close_button = Button(title_bar, text='X', command= login_wn.destroy,bg = "#2e2e2e",padx = 2,pady = 2,activebackground='red',bd = 0,font="bold",fg='white',highlightthickness=0)

    # a canvas for the main area of the window
    

    # pack the widgets
    title_bar.pack(expand=1, fill=X)
    close_button.pack(side=RIGHT)
    xwin=None
    ywin=None
    # bind title bar motion to the move window function

    def move_window(event):
        login_wn.geometry('+{0}+{1}'.format(event.x_login_wn, event.y_login_wn))
    def change_on_hovering(event):
        global close_button
        close_button['bg']='red'
    def return_to_normalstate(event):
        global close_button
    close_button['bg']='#2e2e2e'
    
    
    title_bar.bind('<B1-Motion>', move_window)
    close_button.bind('<Enter>',change_on_hovering)
    close_button.bind('<Leave>',return_to_normalstate)
    """
    def Sig(event):
        login_wn.destroy()
        Sign_up()
    ft1= tkFont.Font(family='Times',size=15)
    frame  =  Frame(login_wn,bg="#202124")
    frame.pack()

    l_user =  Label(frame,text="USERNAME",bg="#202124",fg="#877f86",font=ft1)
    l_user.pack(side= TOP)

    pas =  Entry(frame,text="password",width=40)
    pas.pack()
    pas.bind("<Leave>",passw)

    l_user1 =  Label(frame,text="PASSWORD",bg="#202124",fg="#877f86",font=ft1)
    l_user1.pack()

    user =  Entry(frame,text="user",width=40)
    user.pack()
    user.bind("<Leave>",usern)
    btn  =  Button(frame,text="login",)
    login_wn.config(bg="#202124")
    btn.pack()
    btn1  =  Button(frame,text="Sign_up",)
    btn1.pack()
    btn1.bind("<Button-1>",Sig)

    btn.bind("<Button-1>",run)
    btn["cursor"] = "circle"
    btn["bg"]="#e612bb"
    btn["fg"]="#FFFFFF"
    ft = tkFont.Font(family='Times',size=15)


    btn["font"] = ft
    login_wn.mainloop()




login1()



