import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
import random
import winsound
import csv
import os
from datetime import datetime

MOTIVATIONAL_QUOTES = [
    "🚀 Keep going, coder!",
    "💡 You can do it!",
    "🔥 Stay focused and code on!",
    "🐞 Every bug is a lesson!",
    "⏳ Great things take time!",
    "🤖 Believe in your code!",
    "🏆 Progress, not perfection!",
    "🔍 Debugging is fun!",
    "🎯 You’re almost there!",
    "🛠️ Trust the process!"
]

PROGRESS_COLORS = ["#FF4B4B", "#FF914D", "#FFD93D", "#6BCB77", "#4D96FF"]

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "log_coding.csv")

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⏳ Coding Timer")
        self.root.geometry("800x500")
        self.root.configure(bg="#181c20")
        self.fullscreen = False
        self.running = False
        self.paused = False

        # Style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TLabel", background="#181c20", foreground="#e0e0e0", font=("Segoe UI", 12))
        self.style.configure("TButton", font=("Segoe UI", 11), padding=6)
        self.style.configure("Accent.TButton", background="#4D96FF", foreground="white", borderwidth=0)
        self.style.map("Accent.TButton", background=[("active", "#2563eb")])
        self.style.configure("Danger.TButton", background="#FF4B4B", foreground="white", borderwidth=0)
        self.style.map("Danger.TButton", background=[("active", "#b91c1c")])
        self.style.configure("TProgressbar", thickness=20, troughcolor="#23272e", background="#4D96FF")

        # Timer label (besar di tengah)
        self.label = tk.Label(self.root, text="25:00", font=("Segoe UI Black", 90), fg="#4D96FF", bg="#181c20")
        self.label.pack(pady=(40, 10))

        # Progressbar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=600, mode="determinate", style="TProgressbar")
        self.progress.pack(pady=(0, 20))

        # Quote label
        self.quote_label = tk.Label(self.root, text=random.choice(MOTIVATIONAL_QUOTES), font=("Segoe UI Italic", 12), fg="#FFD93D", bg="#181c20", wraplength=700, justify="center")
        self.quote_label.pack(pady=(0, 20))

        # Time input
        self.time_frame = tk.Frame(self.root, bg="#181c20")
        self.time_frame.pack()
        tk.Label(self.time_frame, text="⏱️ Set Minutes:", bg="#181c20", fg="#e0e0e0").pack(side="left")
        self.minute_var = tk.StringVar(value="25")
        self.minute_entry = ttk.Entry(self.time_frame, textvariable=self.minute_var, width=5)
        self.minute_entry.pack(side="left", padx=5)
        self.add_btn = ttk.Button(self.time_frame, text="➕", width=2, command=self.add_minute, style="Accent.TButton")
        self.add_btn.pack(side="left", padx=(5, 0))
        self.sub_btn = ttk.Button(self.time_frame, text="➖", width=2, command=self.sub_minute, style="Danger.TButton")
        self.sub_btn.pack(side="left", padx=(2, 0))

        # Buttons
        self.btn_frame = tk.Frame(self.root, bg="#181c20")
        self.btn_frame.pack(pady=(20, 0))
        self.start_btn = ttk.Button(self.btn_frame, text="▶️ Start", command=self.start_timer, style="Accent.TButton")
        self.start_btn.pack(side="left", padx=6)
        self.pause_btn = ttk.Button(self.btn_frame, text="⏸️ Pause", command=self.pause_timer, state="disabled")
        self.pause_btn.pack(side="left", padx=6)
        self.resume_btn = ttk.Button(self.btn_frame, text="⏯️ Resume", command=self.resume_timer, state="disabled")
        self.resume_btn.pack(side="left", padx=6)
        self.reset_btn = ttk.Button(self.btn_frame, text="🔄 Reset", command=self.reset_timer, style="Danger.TButton")
        self.reset_btn.pack(side="left", padx=6)

        self.exit_btn = ttk.Button(self.root, text="🖥️ Toggle Fullscreen", command=self.toggle_fullscreen, style="Accent.TButton")
        self.exit_btn.pack(pady=(20, 10))

        self.total_seconds = 25 * 60
        self.initial_seconds = 25 * 60
        self.quote_updater = None
        self.update_quote()

    def update_display(self):
        mins, secs = divmod(self.total_seconds, 60)
        self.label.config(text=f"{mins:02d}:{secs:02d}")
        elapsed = self.initial_seconds - self.total_seconds
        percent = (elapsed / self.initial_seconds) * 100 if self.initial_seconds else 0
        self.progress['value'] = percent
        color_idx = min(int(percent // 25), len(PROGRESS_COLORS) - 1)
        self.style.configure("TProgressbar", background=PROGRESS_COLORS[color_idx])

    def update_quote(self):
        self.quote_label.config(text=random.choice(MOTIVATIONAL_QUOTES))
        self.quote_updater = self.root.after(7000, self.update_quote)

    def stop_quote_update(self):
        if self.quote_updater:
            self.root.after_cancel(self.quote_updater)
            self.quote_updater = None

    def play_sound(self):
        winsound.Beep(1000, 400)

    def notify_done(self):
        messagebox.showinfo("Timer Done", "⏰ Time's up! Take a break!\n\n" + random.choice(MOTIVATIONAL_QUOTES))

    def countdown(self):
        while self.running and self.total_seconds > 0:
            if self.paused:
                time.sleep(0.1)
                continue
            time.sleep(1)
            self.total_seconds -= 1
            self.root.after(0, self.update_display)
        if self.total_seconds == 0:
            self.root.after(0, lambda: self.label.config(text="⏰ Done!", fg="#FF4B4B"))
            self.root.after(0, self.play_sound)
            self.root.after(0, self.notify_done)
            self.root.after(0, self.save_session_log)
        self.root.after(0, lambda: self.start_btn.config(state="normal"))
        self.root.after(0, lambda: self.pause_btn.config(state="disabled"))
        self.root.after(0, lambda: self.resume_btn.config(state="disabled"))

    def start_timer(self):
        try:
            minutes = int(self.minute_var.get())
            if minutes <= 0:
                raise ValueError
            self.total_seconds = minutes * 60
            self.initial_seconds = self.total_seconds
        except ValueError:
            self.quote_label.config(text="⚠️ Please enter a valid positive number!")
            return
        self.running = True
        self.paused = False
        self.update_display()
        self.label.config(fg="#4D96FF")
        self.start_btn.config(state="disabled")
        self.pause_btn.config(state="normal")
        self.resume_btn.config(state="disabled")
        self.progress['value'] = 0
        threading.Thread(target=self.countdown, daemon=True).start()

    def pause_timer(self):
        if self.running:
            self.paused = True
            self.pause_btn.config(state="disabled")
            self.resume_btn.config(state="normal")
            self.quote_label.config(text="⏸️ Paused! Stretch, hydrate, or look away from screen 👀")

    def resume_timer(self):
        if self.running and self.paused:
            self.paused = False
            self.pause_btn.config(state="normal")
            self.resume_btn.config(state="disabled")
            self.quote_label.config(text="💻 Back to coding! 🚀")

    def reset_timer(self):
        self.running = False
        self.paused = False
        self.stop_quote_update()
        try:
            minutes = int(self.minute_var.get())
            if minutes <= 0:
                raise ValueError
            self.total_seconds = minutes * 60
            self.initial_seconds = self.total_seconds
        except ValueError:
            self.total_seconds = 25 * 60
            self.initial_seconds = 25 * 60
        self.update_display()
        self.label.config(fg="#4D96FF")
        self.quote_label.config(text=random.choice(MOTIVATIONAL_QUOTES))
        self.start_btn.config(state="normal")
        self.pause_btn.config(state="disabled")
        self.resume_btn.config(state="disabled")
        self.progress['value'] = 0
        self.update_quote()

    def add_minute(self):
        self.total_seconds += 60
        self.initial_seconds += 60
        self.update_display()

    def sub_minute(self):
        if self.total_seconds > 60:
            self.total_seconds -= 60
            self.initial_seconds -= 60
            self.update_display()

    def save_session_log(self):
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        duration_min = int(self.initial_seconds / 60)
        with open(LOG_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([now, "Fokus", f"{duration_min} menit"])

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.root.attributes('-fullscreen', self.fullscreen)

root = tk.Tk()
app = TimerApp(root)
root.mainloop()
