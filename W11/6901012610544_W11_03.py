import tkinter
def multiply():
    num1 = float( entry1.get() )
    num2 = float( entry2.get() )
    result = num1 * num2
    label.config( text=result )



if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("My tk App")
    window.geometry("500x500")

    label = tkinter.Label(window, text="Hello")
    label.pack()

    entry1 = tkinter.Entry(window)
    entry1.pack()

    entry2 = tkinter.Entry(window)
    entry2.pack()

    button = tkinter.Button(window, text="Multiply",
command=multiply )
    button.pack( pady=40 )


    window.mainloop()