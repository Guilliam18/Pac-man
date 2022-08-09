import tkinter as tk
from tkinter import ttk

def main():
    gui = tk.Tk()
    gui.title("Pac-Man")
    gui.geometry('1200x800+400-200')
    gui.iconbitmap('./Pictures/icon.ico')
    gui['bg']='black'
    gui.mainloop()

if __name__ == "__main__":
    main()