import ttkbootstrap as ttk
from ttkbootstrap.constants import *
def calculate_BMI () :
    height_cm = int(height_int.get())
    weight = int(weight_int.get())
    height_m = height_cm/100
    return(round(weight/height_m**2 , 2))
def age_max_BMI():
    BMI = calculate_BMI()
    if BMI < 18.5 :
        return(f"the BMI is : {calculate_BMI()} the result is : underweight")
    elif 18.5 < BMI < 24.5 :
        return(f"the BMI is : {calculate_BMI()} the result is : healthy weight")
    elif 24.5 < BMI < 29.9 :
        return(f"the BMI is : {calculate_BMI()} the result is : overweight")
    else :
        return(f"the BMI is : {calculate_BMI()} the result is : fat")    
def girl_BMI () :
    BMI = calculate_BMI()
    if BMI < 18.3 :
        return(f"the BMI is : {calculate_BMI()} the result is : underweight")
    elif 18.3 < BMI < 22.7 :
        return(f"the BMI is : {calculate_BMI()} the result is : healthy weight")
    elif 22.7 < BMI < 26.5 :
        return(f"the BMI is : {calculate_BMI()} the result is : overweight")
    else :
        return(f"the BMI is : {calculate_BMI()} the result is : fat")
def boy_BMI () :
    BMI = calculate_BMI()
    if BMI < 18.7 :
        return(f"the BMI is : {calculate_BMI()} the result is : underweight")
    elif 18.7 < BMI < 22.2 :
        return(f"the BMI is : {calculate_BMI()} the result is : healthy weight")
    elif 22.2 < BMI < 24.7 :
        return(f"the BMI is : {calculate_BMI()} the result is : overweight")
    else :
        return("fat") 
def male_female () :
    age_boy= ttk.Checkbutton(window, text="boy ", bootstyle="secondary", command=boy_BMI)
    age_boy.grid(column=0, row=5, sticky=ttk.EW, padx=10, pady=5)
    age_girl = ttk.Checkbutton(window, text='girl', bootstyle="secondary", command=girl_BMI )
    age_girl.grid(column=0, row=6, sticky=ttk.EW, padx=10, pady=5)
#window---------------
window = ttk.Window("BMI ","solar", resizable=(False, False))
BMI_lbl = ttk.Label(window, text="BMI_Calculation")
BMI_lbl.grid(columnspan=2, row=0, sticky=ttk.N, padx=20, pady=5)
#height---------------
height_lbl = ttk.Label(window, text="height(cm) : ")
height_lbl.grid(column=0, row=1, sticky=ttk.W, padx=10, pady=5)
height_int =ttk.Entry(window,bootstyle="success", text="Example : 170 cm")
height_int.grid(column=1, row=1, sticky=ttk.W, padx=10, pady=5)
#weight----------------
weight_lbl = ttk.Label(window, text="weight(kg) : ")
weight_lbl.grid(column=0, row=2, sticky=ttk.W, padx=10, pady=5)
weight_int = ttk.Entry(window, bootstyle="success", text="Example : 45 kg" )
weight_int.grid(column=1, row=2, sticky=ttk.W, padx=10, pady=5)
#age-------------------
age_btn= ttk.Checkbutton(window, text="age > 19 ", bootstyle="secondary", command=age_max_BMI)
age_btn.grid(column=0, row=3, sticky=ttk.EW, padx=10, pady=5)
age_btn_1 = ttk.Checkbutton(window, text='age < 19 ', bootstyle="secondary",command=male_female )
age_btn_1.grid(column=0, row=4, sticky=ttk.EW, padx=10, pady=5)
#apply-----------------
submit_btn = ttk.Button(window, bootstyle="danger" , text="apply")
submit_btn.grid(columnspan=2, row=7, sticky=ttk.EW, padx=10, pady=5)
window.mainloop()