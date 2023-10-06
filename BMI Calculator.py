import customtkinter
import tkinter
from tkinter import messagebox 

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("310x185")
app.title("BMI Calculator")
app.config(padx=20,pady=20)

def calculate():
    weight=float(weight_entry.get())
    height_in_feet=float(height_entry.get())
    height=(height_in_feet)*0.3048


    bmi = weight/(height**2)
    bmi = round(bmi,1)

    if(bmi<18.5):
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Underweight')

    elif(24.9>=bmi>=18.5):
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Normal')

    elif(24.9>bmi):
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Overweight')

weight_label = customtkinter.CTkLabel(master = app ,text="Weight (kg) : ",pady=20,padx=20)
height_label = customtkinter.CTkLabel(master=app,text="Height (feet) : ",pady=20,padx=20)
weight_label.grid(column=0,row=0)
height_label.grid(column=0,row=1)

weight_entry = customtkinter.CTkEntry(master=app,corner_radius=10)
height_entry = customtkinter.CTkEntry(master=app,corner_radius=10)

weight_entry.grid(column=1,row=0)
height_entry.grid(column=1,row=1)

submit_button = customtkinter.CTkButton(master=app,text="Calculate",command=calculate)
submit_button.grid(columnspan=2,row=2,pady=20,padx=60)

app.mainloop()
