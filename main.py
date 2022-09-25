from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✅"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
terms_count, start, timer_counter = 8, False, None

# -------------------------------functions-----------------------------------


def timer(count_down):
    global timer_counter
    if count_down >= 0:
        minutes = count_down // 60
        seconds = count_down % 60
        if minutes < 10:
            minutes = f"0{minutes}"
        if seconds < 10:
            seconds = f"0{seconds}"
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        timer_counter = window.after(10, timer, count_down - 1)
    else:
        check_marks.config(text=CHECK_MARK * (4 - int(terms_count/2)))
        timer_loop()


def timer_loop():
    global terms_count, start
    terms_count -= 1
    if terms_count != 0:
        if terms_count % 2 == 1:
            label_up.config(text="Work", fg=GREEN)
            timer(WORK_MIN * 60)
        else:
            label_up.config(text="Break", fg=RED)
            timer(SHORT_BREAK_MIN * 60)
    else:
        terms_count = 8
        label_up.config(text="Break", fg=RED)
        timer(LONG_BREAK_MIN * 60)


def restart_timer():
    global start, terms_count
    window.after_cancel(timer_counter)
    label_up.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    start, terms_count = False, 8


def start_timer():
    global start
    if not start:
        start = True
        timer_loop()


# -------------------------------GUI setup-----------------------------------


window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodora")
window.resizable(False, False)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

label_up = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45, "bold"), bg=YELLOW)
label_up.grid(column=1, row=0)

button_start = Button(text="Start", font=(FONT_NAME, 13, "bold"), command=start_timer)
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", font=(FONT_NAME, 13, "bold"), command=restart_timer)
button_reset.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
