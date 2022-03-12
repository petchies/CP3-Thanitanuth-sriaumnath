from tkinter import *

MainWindow = Tk()

canvas1 = Canvas(MainWindow, width=400, height=500, bg= "blue")
canvas1.pack()

label1 = Label(MainWindow, text = "MengHao Calculator")
label1.config(font= ("helvetica, 20"))
canvas1.create_window(200, 25, window = label1)

entry1 = Entry(MainWindow)
canvas1.create_window(200, 100, window = entry1)

entry2 = Entry(MainWindow)
canvas1.create_window(200, 150, window = entry2)

def summation():
    number1 = entry1.get()
    number2 = entry2.get()
    result_summation = float(number1) + float(number2)
    label2 = Label(MainWindow,text = result_summation)
    label2.config(font=("helvetica, 20"))
    canvas1.create_window(200, 360, window = label2)
    print(result_summation)

def minus():
    number1 = entry1.get()
    number2 = entry2.get()
    result_minus = float(number1) - float(number2)
    label2 = Label(MainWindow,text = result_minus)
    label2.config(font=("helvetica, 20"))
    canvas1.create_window(200, 360, window = label2)



def multiplication():
    number1 = entry1.get()
    number2 = entry2.get()
    result_multiplication = float(number1) * float(number2)
    label2 = Label(MainWindow,text = result_multiplication)
    label2.config(font=("helvetica, 20"))
    canvas1.create_window(200, 360, window = label2)


def divide():
    number1 = entry1.get()
    number2 = entry2.get()
    result_divide = float(number1) / float(number2)
    label2 = Label(MainWindow,text = result_divide)
    label2.config(font=("helvetica, 20"))
    canvas1.create_window(200, 360, window = label2)


button1 = Button(MainWindow, text = "summation", command = summation)
canvas1.create_window(200, 200, window =button1)

button2 = Button(MainWindow, text = "minus", command = minus)
canvas1.create_window(200, 240, window =button2)

button3 = Button(MainWindow, text = "multiplication", command = multiplication)
canvas1.create_window(200, 280, window =button3)

button4 = Button(MainWindow, text = "divide", command = divide)
canvas1.create_window(200, 320, window =button4)

MainWindow.mainloop()