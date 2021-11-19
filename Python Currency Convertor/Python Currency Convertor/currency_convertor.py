from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
from google_currency import convert
import json

root = Tk()
root.title("Currency Convertor")
root.iconbitmap("dollar.ico")
root.config(bg="LightPink")
root.geometry("600x400")

with open ("currency.txt") as f:
    lines = f.readlines()

dictionary = {}
for line in lines:
    parsing = line.split("\t");
    dictionary[parsing[1]] = parsing[2]

def convertor_function():
    try:
        box1 = convert_from_Combobox1.get()
        box2 = convert_from_Combobox2.get()
        code1 = dictionary[box1]
        code2 = dictionary[box2]
        serial = text_var.get()
        main = convert(code1, code2, serial)
        json_python = json.loads(main)
        jsonfix = json_python["amount"]
        text_var1.set(jsonfix)
    except:
        message = messagebox.askretrycancel("A Problem Has Been Occured", "Your amount should only be in Numbers if it is correct then, Please Check your Internet Connection.")


Title = Label(root, text="Currency Convertor", fg="MediumVioletRed",  bg="LightPink", font=("Roboto", 20, "bold"))
Title.place(x=150, y=10)
amount_convert = Label(root, text="Enter the Amount to Convert : ",  fg="#cc313d", bg="LightPink", font=("Roboto", 15, "bold"))
amount_convert.place(x=10, y=70)

text_var = DoubleVar()
convert_entry = Entry(root, width=24 ,text=text_var, fg="DarkOrange", bg="white", font=("Roboto", 15, "bold"))
convert_entry.place(x=310, y=70)

currency_convert = Label(root, text="Select the Currency to Convert Your Amount From : ",  fg="Tomato", bg="LightPink", font=("Roboto", 10, "bold"))
currency_convert.place(x=10, y=120)

slider1 = StringVar()
convert_from_Combobox1 = Combobox(root, width=20, textvariable=slider1, state="readonly", font=("Roboto", 10, "bold"))
convert_from_Combobox1['values'] = [item for item in dictionary.keys()]
convert_from_Combobox1.current(0)
convert_from_Combobox1.place(x=350, y=120)

Lable3 = Label(root, text="Select the Currency to Convert Your Amount To : " , fg="Tomato", bg="LightPink", font=("Roboto", 10, "bold"))
Lable3.place(x=10, y=160)

slider2 = StringVar()
convert_from_Combobox2 = Combobox(root, width=20, textvariable=slider2, state="readonly", font=("Roboto", 10, "bold"))
convert_from_Combobox2['values'] = [item for item in dictionary.keys()]
convert_from_Combobox2.current(1)
convert_from_Combobox2.place(x=350, y=160)

convert_Button = Button(root, bg="Crimson", text="Convert" , fg="#872657", font=("Roboto", 15, "bold"), command=convertor_function, relief = RAISED, cursor="hand2")
convert_Button.place(x=240, y=220)

convert_amount = Label(root, text="Converted Amount Is : ", bg="LightPink", fg="#cc313d", font=("Roboto", 15, "bold"))
convert_amount.place(x=15, y=280)

text_var1 = DoubleVar()
convert_entry1 = Entry(root, textvariable=text_var1, fg="#4B0082", state="readonly",width=27, font=("Roboto", 15, "bold"))
convert_entry1.place(x=240, y=280)

root.mainloop()