from tkinter import *
import math

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
check_mark = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, check_mark
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    check_marks.config(text="")
    check_mark = ""
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0 and reps < 8:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps == 1 or reps == 3 or reps == 5:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps == 7:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, check_mark, timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min >= 0 and count_min <= 9:
        count_min = f"0{count_min}"
    if count_sec >= 0 and count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        reps += 1
        if reps == 1 or reps == 3 or reps == 5 or reps == 7:
            check_mark = check_mark + "✓"
            print(check_mark)
            check_marks.config(text=check_mark)
        start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=500)
window.config(pady=150, padx=200, bg=YELLOW)


timer_label = Label(text="Timer", font=(FONT_NAME, 36, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)


canvas = Canvas(width=200, height=224)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(
    100, 130, text="25:00", fill="white", font=(FONT_NAME, 26, "bold")
)

canvas.config(bg=YELLOW, highlightthickness=0)
canvas.grid(row=1, column=1)

start_button = Button(
    text="Start", highlightthickness=0, bg=PINK, font=(FONT_NAME, 12), command=start
)
start_button.grid(row=2, column=0)

reset_button = Button(
    text="Reset", highlightthickness=0, bg=PINK, font=(FONT_NAME, 12), command=reset
)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()
