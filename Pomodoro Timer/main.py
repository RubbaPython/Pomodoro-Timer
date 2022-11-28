import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 4
LONG_BREAK_MIN = 15
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_TIMER():
  global REPS
  REPS = 0
  window.after_cancel(TIMER)
  canvas.itemconfig(TIMER_text,text="00:00")
  check_label["text"] = ""
  label.config(text="TIMER",fg=GREEN)
  
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_TIMER():
  global REPS
  REPS += 1
  
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60

  if REPS % 8 == 0:
    label.config(text="Long Break",fg=RED)
    count_down(long_break_sec)
  elif REPS % 2 == 0:
    label.config(text="Break",fg=PINK)
    count_down(short_break_sec)      
  else:
    label.config(text="Work",fg=GREEN)
    count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"
  
  canvas.itemconfig(TIMER_text,text=f"{count_min}:{count_sec}")
  if count > 0:
    global TIMER
    TIMER = window.after(1000,count_down,count - 1)
  else:
    start_TIMER()
    if REPS % 2 == 0:
      check_label["text"] += "🍅"
# ---------------------------- UI SETUP ------------------------------- #
window  = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=photo)
TIMER_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

label = Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
label.grid(column=1,row=0)

check_label = Label(bg=YELLOW,font=(FONT_NAME,30,"bold"))
check_label.grid(column=1,row=3)

start_button = Button(text="Start",highlightthickness=0,command=start_TIMER)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_TIMER)
reset_button.grid(column=2,row=2)


window.mainloop()