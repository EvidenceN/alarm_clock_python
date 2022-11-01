# building an alarm clock that uses 12 time intervals instead of 24 hours. 

from tkinter import *
import datetime
import time
import winsound

# a while loop 

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%m/%d/%Y")
        #print("The Set Date is:",date)
        #print("Current Time",now)
        #print("Time input", set_alarm_timer)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("SystemAsterisk",winsound.SND_ALIAS)
            break

def actual_time():
    user_input_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(user_input_time)


clock = Tk()

#print(clock)

clock.title("EvidenceN Alarm Clock")
clock.geometry("600x400")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font=["Arial", 20, "bold"]).place(x=70, y = 10),#,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 190, y=60)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",10,"bold")).place(x=0, y=90)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 25).place(x=150,y=91)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 25).place(x=190,y=91)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 25).place(x=240,y=91)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 30,command = actual_time).place(x =140,y=130)

clock.mainloop()
#Execution of the window.

# Inspiration came from this blog -- https://data-flair.training/blogs/alarm-clock-python/