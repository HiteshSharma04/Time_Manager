from tkinter import *
import math
WORK = 25
SHORT = 5
LONG = 20
reps = 0 
t =None


def reset():
    window.after_cancel(t)
    canva.itemconfig(timer, text="00:00")
    label.config(text="TIMER")
    label1.config(text="")
    global reps
    reps = 0
    button1.config(state="normal")
def timer_count():
    global reps
    reps += 1
    button1.config(state="disabled")
    if reps%8==0:
        count(LONG*60)
        label.config(text="LONG BREAK", fg="blue")
    elif reps%2==0:
        count(SHORT*60)
        label.config(text="SHORT BREAK", fg="gold")
    else:
        count(WORK*60)
        label.config(text="WORK TIME", fg="pink")

def count(a):
    minute = math.floor(a/60)
    second = a % 60
    if second < 10:
        second=f"0{second}"
    if minute < 10:
        minute=f"0{minute}"

    canva.itemconfig(timer, text=f"{minute}:{second}")
    if a > 0:
        global t
        t = window.after(1000, count, a-1)
    else:
        timer_count()
        marks = ""
        for i in range(math.floor(reps/2)):
            marks += "✔"
            label1.config(text=marks)


#     minute = 00
#     second = 00
#     canva.itemconfig(timer, text=f"{minute}:{second}" )




window = Tk()
window.title("Clock")
window.config(padx=100, pady=60, bg="black")

label = Label(text="TIMER", font= ("Courier",60,"bold"), fg="white", highlightthickness=0,bg="black")
label.grid(row=0,column=1)

button1 = Button(text="START", font=("Courier",30,"bold"), fg="green", highlightthickness=0,command=timer_count)
button2 = Button(text="RESET", font=("Courier",30,"bold"), fg="red", highlightthickness=0,command=reset)
button1.grid(row=1,column=0)
button2.grid(row=1,column=2)


label1 = Label(font=("Courier",30,"bold"), fg="green" ,bg="black", highlightthickness=0 )
label1.grid(row=2,column=1)

canva = Canvas(width=400,height=424, bg="black", highlightthickness=0)
pic = PhotoImage(file= "projects/tkinter/cl.png")
canva.create_image(203,212, image= pic)
timer = canva.create_text(203,312, text = "00:00", font=("courier",45,"bold"), fill="red")
canva.grid(row=1,column=1)


window.mainloop()