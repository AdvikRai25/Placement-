import tkinter
import time
import sys
from tkinter import messagebox

def flash_label():
    current_text = res.cget("text")
    if current_text == "":
        res.config(text=res.full_text)
    else:
        res.config(text="")
    root.after(500, flash_label)

def cal_bmi():
    h = float(ht_val.get())
    w = float(wt_val.get())
    h1 = h/100
    bmi = w/h1**2
    bmi = round(bmi,2)
    if(bmi<18.9):
        status = "Underweight"
        messagebox.showwarning("BMI Alert", "Your BMI indicates you are underweight.\nConsider consulting a doctor.")
    elif(bmi>=18.9 and bmi<24.9):
        status = "Normal"
    elif(bmi>=24.9 and bmi<29.9):
        status = "Overweight"
    else:
        status = "Obese"
        messagebox.showwarning("BMI Alert",
                               "Your BMI indicates obesity.\nIt's advisable to consult a healthcare provider.")
    result_text = f"Your BMI is {bmi}. You are {status}."
    res.full_text = result_text
    res.config(text=result_text, foreground="black")
    flash_label()

root = tkinter.Tk()
root.geometry("500x500")
root.title("BMI Calculator")
root.config(background = "#F0F0F0")

head = tkinter.Label(root, text = "BMI Calculator", font = ("Times New Roman", 20, "bold"))
head.pack(pady=10)
fr = tkinter.Frame(root)
fr.pack(pady=10)

ht = tkinter.Label(fr, text = "Height (in cm)", font = ("Arial", 10),bg = "#FCE69D")
ht.grid(row = 1, column = 0, padx = 5, pady = 5)

ht_val = tkinter.Entry(fr, bg = "#F0F0F0")
ht_val.grid(row = 1, column = 1, padx = 5, pady = 5)

wt = tkinter.Label(fr, text = "Weight (in kg)", font = ("Arial", 10),bg = "#FCE69D")
wt.grid(row = 2, column = 0, padx = 5, pady = 5)

wt_val = tkinter.Entry(fr, bg = "#F0F0F0")
wt_val.grid(row = 2, column = 1, padx = 5, pady = 5)

bt = tkinter.Button(fr, text = "Calculate", font=("Arial", 12, "bold"), bg="#98b97b", command=cal_bmi)
bt.grid(row = 3, column = 0, padx = 5, pady = 5)

res = tkinter.Label(text="Know your BMI")
res.pack(pady=10)
root.mainloop()