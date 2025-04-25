# game.py

import pyautogui
import webbrowser
import tkinter as tk
import time
import threading
import random


def open_rickroll():
    webbrowser.open("https://www.youtube.com/watch?v=2qBlE2-WL60")

def move_mouse_randomly():
    while True:
        x = random.randint(0, pyautogui.size().width)
        y = random.randint(0, pyautogui.size().height)
        pyautogui.moveTo(x, y, duration=0.2)
        time.sleep(0.2)

def popup_spam():
    for _ in range(10):
        top = tk.Tk()
        top.title("Surprise!")
        msg = tk.Label(top, text="You just got Rickrolled! 🤡", font=("Arial", 14))
        msg.pack()
        top.geometry(f"300x100+{random.randint(0,500)}+{random.randint(0,500)}")
        threading.Thread(target=top.mainloop).start()
        time.sleep(0.5)

def fake_game():
    win = tk.Tk()
    win.title("Cool Game.exe")
    win.geometry("400x300")
    label = tk.Label(win, text="Loading...", font=("Arial", 18))
    label.pack(pady=50)
    win.after(3000, lambda: label.config(text="ERROR: Fun Overload"))
    win.after(6000, lambda: win.destroy())
    win.mainloop()

def main():
    threading.Thread(target=open_rickroll).start()
    threading.Thread(target=move_mouse_randomly, daemon=True).start()
    popup_spam()
    fake_game()

if __name__ == "__main__":
    main()
