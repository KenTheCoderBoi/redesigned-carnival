from tkinter import *
import random
from PIL import ImageTk,Image
root=Tk()
root.title("hi")
root.geometry("600x400")
root.configure(background="yellow")
turn=1
score1=0   
score2=0
img= ImageTk.PhotoImage(Image.open ("dice1.4.jpg"))
def player1():
    global turn
    if turn==1:
        global score1
        roll=random.randint(1,6)
        score1=score1+roll
        player1_score["text"]=score1
        roll_label["text"]="player 1 rolled a "+str(roll)+"."
        turn=2
    else:
        roll_label["text"]="not your turn!"
        score1=score1-1
        player1_score["text"]=score1
def player2():
    global turn
    if turn==2:
        global score2
        roll=random.randint(1,6)
        score2=score2+roll
        player2_score["text"]=score2
        roll_label["text"]="player 2 rolled a "+str(roll)+"."
        turn=1
    else:
        roll_label["text"]="not your turn!"
        score2=score2-1
        player2_score["text"]=score2
def free():
    global score2
    global score1
    score2=score2+0.001
    score1=score1+0.001
    player2_score["text"]=score2
    player1_score["text"]=score1
    
player1=Button(root,text="Player 1",command=player1)
player1.place(relx=0.1,rely=0.4,anchor=CENTER)

player2=Button(root,text="Player 2",command=player2)
player2.place(relx=0.9,rely=0.4,anchor=CENTER)

point=Button(root,text="free 0.001 points!",command=free)
point.place(relx=0.5,rely=0.7,anchor=CENTER)

player1_score=Label(root,text="")
player1_score.place(relx=0.1,rely=0.5,anchor=CENTER)

player2_score=Label(root,text="")
player2_score.place(relx=0.9,rely=0.5,anchor=CENTER)

roll_label=Label(root,text="")
roll_label.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()