import tkinter
import math

import _tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    timer
    window.after_cancel(timer)
    label1.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    label2.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # IF IT'S THE 8TH REP:
    if reps % 8 == 0:
        label1.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    # IF IT'S THE 2ND/ 4TH/ 6TH REP:
    elif reps % 2 == 0:
        label1.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    # IF IT'S THE 1ST/ 3RD/ 5TH/ 7TH REP:
    else:
        label1.config(text="WORK", fg=GREEN)
        count_down(work_sec)

    count_down(25 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        label2.config(text=marks, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #

# WINDOW
window = tkinter.Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

# TIMER LABEL
label1 = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label1.grid(column=1, row=0)

# TOMATO IMAGE
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# START BUTTON
button1 = tkinter.Button(text="START", command=start_timer)
button1.grid(column=0, row=2)

# CHECKMARK
label2 = tkinter.Label(bg=YELLOW, font="bold")
label2.grid(column=1, row=3)

# RESET BUTTON
button2 = tkinter.Button(text="RESET", command=reset_timer)
button2.grid(column=2, row=2)

window.mainloop()
