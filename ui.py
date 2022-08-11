from tkinter import *

window = Tk()

window.title("snomai")

window.geometry('1280x720')

lbl = Label(window, text="Select Project Type", padx=1, pady=1)
lbl.grid(column=0, row=0)

recut_btn = Button(window, text="recut")
recut_btn.grid(column=0, row=1)

voiceover_btn = Button(window, text="voiceover")
voiceover_btn.grid(column=1, row=1)


window.mainloop()