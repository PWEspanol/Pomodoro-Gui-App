from tkinter import *
import math
from playsound import playsound
from gtts import gTTS

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Set you time wishes
WORK_MIN = 0.05
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 20
reps = 0 
mark = 0
timer = None

# ---------------------------- PLAYSOUND ------------------------------- #

def convert_short_brake_to_audio():
    text = "It is time for short brake"
    global audio_short
    audio_short = gTTS(text)
    audio_short.save("shortbrake.mp3")


convert_short_brake_to_audio()

def convert_long_brake_to_audio():
    text = "It is time for loooong brake brake"
    global audio_long
    audio_long = gTTS(text)
    audio_long.save("longbrake.mp3")

convert_long_brake_to_audio()


def playaudio(audio):
    playsound(audio)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)

    my_timer.config(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
    check_mark.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 22, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0 
    


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def button_start_clicked():
    global reps
    reps += 1 

    work_sec = 60 * WORK_MIN
    short_break_sec = 60 * SHORT_BREAK_MIN
    long_break_sec = 60 * LONG_BREAK_MIN

    if reps % 8 == 0:
        count_down(long_break_sec)
        my_timer.config(text="Break", fg=RED)
        playaudio("longbrake.mp3")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_timer.config(text="Break", fg=PINK)
        playaudio(("shortbrake.mp3"))
    else:
        count_down(work_sec)
        my_timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    if seconds == 0:
        seconds = "00"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0: 
        global timer 
        timer = window.after(1000, count_down, count - 1)
    else:
        button_start_clicked()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomidoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
my_timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
my_timer.grid(row=0, column=1) 

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 22, "bold"))
check_mark.grid(row=3, column=1)
     
    
        

    

# Buttons


button_start = Button(text="Start", command=button_start_clicked, highlightthickness=0)
button_start.grid(row=2, column=0)


button_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(row=2, column=2)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 109, image=tomato_img)
timer_text = canvas.create_text(100, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



# ✔





window.mainloop()
