from tkinter import *
import time
import winsound

window = Tk()
window.geometry("500x600")
window.title("Deep Work Timer")

current_time = 5400
running = False


def seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds


def start():
    global current_time, running
    running = True
    while current_time > 0 and running:
        hours, minutes, seconds = seconds_to_hms(current_time)
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        timer.config(text=time_str)
        window.update()
        time.sleep(1)
        current_time -= 1
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)


def stop():
    global running
    running = False


def restart():
    global running, current_time
    running = False
    current_time = 5400
    timer.config(text="01:30:00")


timer = Label(window, text="01:30:00", width=16, height=6, font=("Arial", 40, "bold"))
timer.grid(column=1, row=0)

start_button = Button(window, text="START", height=2, width=10, command=start, cursor="hand2")
start_button.grid(column=1, row=1, pady=5)

stop_button = Button(window, text="STOP", height=2, width=10, command=stop, cursor="hand2")
stop_button.grid(column=1, row=2, pady=5)

restart_button = Button(window, text="RESTART", height=2, width=10, cursor="hand2", command=restart)
restart_button.grid(column=1, row=3, pady=5)

window.mainloop()


