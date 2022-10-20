from tkinter import *

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


def reset():
    global reps
    reps = 0
    # Cancelling the timer function.
    canvas.after_cancel(timer)
    check1.place(x=1000, y=1000)
    check2.place(x=1000, y=1000)
    check3.place(x=1000, y=1000)
    check4.place(x=1000, y=1000)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global reps
    reps += 1
    if reps in [1, 3, 5, 7]:
        timer_label.config(text="Work", fg=GREEN)
        timer_label.place(x=235, y=80)
        if reps == 1:
            check1.place(x=230, y=400)
        if reps == 3:
            check2.place(x=260, y=400)
        if reps == 5:
            check3.place(x=290, y=400)
        if reps == 7:
            check4.place(x=320, y=400)
        count_down(WORK_MIN * 60)
    if reps in [2, 4, 6, 8]:
        timer_label.config(text="Break", fg=PINK)
        timer_label.place(x=230, y=80)
        count_down(SHORT_BREAK_MIN * 60)
    if reps == 9:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    if reps == 10:
        quit()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    if count > -1:
        minutes = count // 60
        seconds = count % 60
        if seconds < 10:
            seconds = "0" + str(seconds)
        if minutes < 10:
            minutes = "0" + str(minutes)
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        global timer
        timer = tv.after(1000, count_down, count - 1)
    else:
        start()

# ---------------------------- UI SETUP ------------------------------- #


tv = Tk()
tv.title("Pomodoro")
tv.minsize(width=600, height=600)
tv.maxsize(width=600, height=600)
tv.config(bg=YELLOW)


canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.place(x=200, y=150)

timer_label = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
timer_label.place(x=220, y=80)

check1 = Label(text="✔", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check2 = Label(text="✔", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check3 = Label(text="✔", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check4 = Label(text="✔", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)

start_button = Button(text="Start", height=1, width=6, relief="groove", bg="white", command=start)
start_button.place(x=130, y=370)

reset_button = Button(text="Reset", height=1, width=6, relief="groove", bg="white", command=reset)
reset_button.place(x=420, y=370)


tv.mainloop()
