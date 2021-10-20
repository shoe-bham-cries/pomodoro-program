import tkinter as tki

#  THEME AND OTHER CONSTANTS#
# WORK_SEC = 1500s = 25 mins
# SHORT_BREAK_SEC = 300 = 5 mins
# LONG_BREAK_SEC = 1800 = 30 mins
BLACK = "#000000"
RUSSIAN_VIOLET = "#3E065F"
PURPLE = "#700B97"
FRENCH_VIOLET = "#8E05C2"
FONT_NAME = "Courier"
WORK_SEC = 1500
SHORT_BREAK_SEC = 300
LONG_BREAK_SEC = 1800
ICON = "🍅"
REPS = 0
watch = None  # Had to create empty variable which runs down timer so it can be used between reset_action and set_action


# Reset Button Function #


def reset_action():
    global REPS
    window.after_cancel(watch)
    pomo.config(text="POMODORO")
    canvas.itemconfig(timer, text="00:00")
    icon.config(text="")
    REPS = 0


# Start Button Function#


def start_action():
    global REPS
    REPS += 1
    if REPS % 2 != 0:
        count_down(WORK_SEC)
        pomo.config(text="Work", font=(FONT_NAME, 25, "bold"), bg=BLACK, fg=PURPLE, padx=10, pady=10)
        icon.config(text=((REPS // 2) + 1) * ICON)
    elif REPS % 2 == 0 and REPS % 8 != 0:
        count_down(SHORT_BREAK_SEC)
        pomo.config(text="Short Break", font=(FONT_NAME, 25, "bold"), bg=BLACK, fg=RUSSIAN_VIOLET, padx=10, pady=10)
    else:
        count_down(LONG_BREAK_SEC)
        pomo.config(text="Long Break", font=(FONT_NAME, 25, "bold"), bg=BLACK, fg=FRENCH_VIOLET, padx=10, pady=10)


# Countdown Function #


def count_down(seconds):
    global REPS
    minutes, sec = divmod(seconds, 60)
    canvas.itemconfig(timer, text="%02d:%02d" % (minutes, sec))
    if seconds > 0:
        global watch
        watch = window.after(1000, count_down, (seconds - 1))
    elif REPS != 8:
        start_action()


# Tkinter UI setup  #
window = tki.Tk()
window.title("Time Manager")
window.config(padx=90, pady=40, bg=BLACK)

pomo = tki.Label(text="POMODORO", font=(FONT_NAME, 25, "bold italic"), bg=BLACK, fg=RUSSIAN_VIOLET, padx=10, pady=10)
pomo.grid(column=1, row=0)

start = tki.Button(text="START", fg=PURPLE, command=start_action, highlightthickness=0)
start.grid(column=0, row=2)

reset = tki.Button(text="RESTART", fg=PURPLE, command=reset_action, highlightthickness=0)
reset.grid(column=2, row=2)

icon = tki.Label(font=(FONT_NAME, 15, "normal"), bg=BLACK, fg=FRENCH_VIOLET, padx=10, pady=10)
icon.grid(column=1, row=3)

img = tki.PhotoImage(file="tomato.png")
canvas = tki.Canvas(width=210, height=213, bg=BLACK, highlightthickness=0)
canvas.create_image(112, 110, image=img)
timer = canvas.create_text(100, 125, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1, padx=50, pady=50)

window.mainloop()
