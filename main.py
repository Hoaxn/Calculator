from tkinter import *

expression = ""


def press(num):
    global expression

    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression

        total = str(eval(expression))
        equation.set(total)

        expression = ""

    except:
        equation.set("error")
        expression = ""


def clear():
    global expression

    expression = ""
    equation.set("0")


root = Tk()
root.title("Calculator")
root.geometry("355x475")
root.configure(bg="#ff9900")
root.iconbitmap("calc.ico")
root.resizable(False, False)

buttonFrame = Frame(root, bg="#ff9900")
buttonFrame.pack()

equation = StringVar()
equation.set("0")

expressionField = Entry(buttonFrame, textvariable=equation, justify="right", font=("arial", 20, "bold"))

button1 = Button(buttonFrame, font=("times new roman", 11), text='1', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                 command=lambda: press(1), height=3, width=9)
button2 = Button(buttonFrame, font=("times new roman", 11), text='2', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                 command=lambda: press(2), height=3, width=9)
button3 = Button(buttonFrame, font=("times new roman", 11), text='3', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                 command=lambda: press(3), height=3, width=9)
plus = Button(buttonFrame, font=("times new roman", 11), text='+', bd=1, relief="ridge", fg="black", bg="#ffcc80",
              command=lambda: press("+"), height=3, width=9)
button4 = Button(buttonFrame, font=("times new roman", 11), text='4', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                 command=lambda: press(4), height=3, width=9)
button5 = Button(buttonFrame, font=("times new roman", 11), text='5', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                 command=lambda: press(5), height=3, width=9)
button6 = Button(buttonFrame, font=("times new roman", 11), text='6', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                 command=lambda: press(6), height=3, width=9)
minus = Button(buttonFrame, font=("times new roman", 11), text='-', bd=1, relief="ridge", fg="black", bg="#ffcc80",
               command=lambda: press("-"), height=3, width=9)
button7 = Button(buttonFrame, font=("times new roman", 11), text='7', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                 command=lambda: press(7), height=3, width=9)
button8 = Button(buttonFrame, font=("times new roman", 11), text='8', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                 command=lambda: press(8), height=3, width=9)
button9 = Button(buttonFrame, font=("times new roman", 11), text='9', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                 command=lambda: press(9), height=3, width=9)
multiply = Button(buttonFrame, font=("times new roman", 11), text='*', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                  command=lambda: press("*"), height=3, width=9)
button0 = Button(buttonFrame, font=("times new roman", 11), text='0', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                 command=lambda: press(0), height=3, width=9)
decimal = Button(buttonFrame, font=("times new roman", 11), text='.', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                 command=lambda: press("."), height=3, width=9)
clear = Button(buttonFrame, font=("times new roman", 11), text='C', bd=1, relief="ridge", fg="black", bg="#ffcc80",
               command=clear, height=3, width=9)
divide = Button(buttonFrame, font=("times new roman", 11), text='/', bd=1, relief="ridge", fg="black", bg="#ffcc80",
                command=lambda: press("/"), height=3, width=9)
equal = Button(buttonFrame, font=("times new roman", 11), text='=', bd=1, relief="ridge", fg="black", bg="#ffcc80",
               command=equalpress, height=3, width=9)

expressionField.grid(row=0, column=0, ipadx=7, columnspan=4, ipady=25, pady=15)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
plus.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
minus.grid(row=2, column=3)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
multiply.grid(row=3, column=3)

button0.grid(row=4, column=0)
decimal.grid(row=4, column=1)
clear.grid(row=4, column=2)
divide.grid(row=4, column=3)

equal.grid(row=5, column=0, columnspan=4, sticky="nsew", pady=5)

root.mainloop()
