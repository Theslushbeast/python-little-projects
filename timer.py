import tkinter as tk
import time

# Constants
WORK_MIN = 25
BREAK_MIN = 5

# Global variables
timer_running = False
timer_id = None

def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        countdown(WORK_MIN * 60)

def countdown(count):
    global timer_id
    minutes = count // 60
    seconds = count % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        timer_id = window.after(1000, countdown, count - 1)
    else:
        start_break()

def start_break():
    timer_label.config(text="Break Time!")
    window.after(1000, countdown_break, BREAK_MIN * 60)

def countdown_break(count):
    global timer_id
    minutes = count // 60
    seconds = count % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        timer_id = window.after(1000, countdown_break, count - 1)
    else:
        timer_label.config(text="Time to Work!")
        global timer_running
        timer_running = False

def reset_timer():
    global timer_running, timer_id
    if timer_id:
        window.after_cancel(timer_id)
    timer_running = False
    timer_label.config(text="00:00")

# GUI Setup
window = tk.Tk()
window.title("🍅 Pomodoro Timer")
window.geometry("300x200")

timer_label = tk.Label(window, text="00:00", font=("Arial", 40))
timer_label.pack(pady=20)

start_button = tk.Button(window, text="▶ Start", command=start_timer)
start_button.pack(side="left", padx=20)

reset_button = tk.Button(window, text="⏹ Reset", command=reset_timer)
reset_button.pack(side="right", padx=20)

window.mainloop()
