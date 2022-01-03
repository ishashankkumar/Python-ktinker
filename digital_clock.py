import tkinter as tk
from tkinter import ttk, Label
import time


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        root  = tk.Tk()
        root.geometry("500x500")
        self.clock_label=Label(root,font=("times",100,"bold"),bg="tomato")
        self.clock_label.grid(row=1,column=2,pady=15,padx=50)
        self.clock()

        digi = Label(root,text="Clock",font="times 36")
        digi.grid(row=0,column=2)

        nota=Label(root,text="Hours   Minutes   Seconds", font="times 30")
        nota.grid(row=3,column=2)

    def clock(self):
        time_now=time.strftime("%H:%M:%S")
        self.clock_label.config(text=time_now)
        self.clock_label.after(200,self.clock)

if __name__ == "__main__":
    app = App()
    app.mainloop()
