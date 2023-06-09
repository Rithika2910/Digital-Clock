import tkinter as tk
from tkinter import font
import time

class DigitalClock(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Digital Clock")

        self.time_label = tk.Label(self, font=("Helvetica", 48), bg="black", fg="white")
        self.time_label.pack(pady=20)

        self.date_label = tk.Label(self, font=("Helvetica", 24), bg="black", fg="white")
        self.date_label.pack(pady=10)

        self.hour_format = tk.StringVar()
        self.hour_format.set("24")

        self.toggle_button = tk.Button(self, text="Toggle Format", command=self.toggle_hour_format)
        self.toggle_button.pack(pady=10)

        self.alarm_entry = tk.Entry(self, font=("Helvetica", 24))
        self.alarm_entry.pack(pady=10)

        self.alarm_button = tk.Button(self, text="Set Alarm", command=self.set_alarm)
        self.alarm_button.pack(pady=10)

        self.update_time()

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        current_date = time.strftime('%A, %B %d, %Y')
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.master.after(1000, self.update_time)

        if self.check_alarm(current_time):
            self.activate_alarm()

    def toggle_hour_format(self):
        if self.hour_format.get() == "24":
            self.hour_format.set("12")
        else:
            self.hour_format.set("24")

    def set_alarm(self):
        alarm_time = self.alarm_entry.get()
        if alarm_time:
            self.alarm_entry.delete(0, tk.END)
            self.alarm_entry.insert(0, "Alarm Set: " + alarm_time)

    def check_alarm(self, current_time):
        alarm_time = self.alarm_entry.get()
        if alarm_time and current_time == alarm_time:
            return True
        return False

    def activate_alarm(self):
        self.toggle_button.config(state=tk.DISABLED)
        self.alarm_button.config(state=tk.DISABLED)
        alarm_label = tk.Label(self, text="ALARM!", font=("Helvetica", 48), bg="black", fg="red")
        alarm_label.pack(pady=10)
        self.master.after(5000, self.reset_alarm)

    def reset_alarm(self):
        self.toggle_button.config(state=tk.NORMAL)
        self.alarm_button.config(state=tk.NORMAL)
        for child in self.winfo_children():
            if isinstance(child, tk.Label):
                child.destroy()

root = tk.Tk()
app = DigitalClock(master=root)
app.pack()
app.mainloop()
