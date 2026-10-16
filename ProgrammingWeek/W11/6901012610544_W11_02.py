import tkinter

window = tkinter.Tk()
window.title("My tk App")
window.geometry("500x500")
label = tkinter.Label(window, text="Hello")
label.pack()

window.mainloop()