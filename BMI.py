import ttkbootstrap as ttk
from ttkbootstrap.constants import *
def age_max () :
    age_btn_1.grid_forget ()
    return(0)
def age_min_boy () :
    return(1) 
def age_min_girl () :
    return(2)
def calculate_BMI () :
    height_cm = int(height_int.get())
    weight = int(weight_int.get())
    height_m = height_cm/100
    return(round(weight/height_m**2 , 2))
def age_max_BMI():
    BMI = calculate_BMI()
    max = age_max()
    if max == 0 :
        if BMI < 18.5 :
            return(f"the BMI is : {calculate_BMI()} the result is : underweight")
        elif 18.5 < BMI < 24.5 :
            return(f"the BMI is : {calculate_BMI()} the result is : healthy weight")
        elif 24.5 < BMI < 29.9 :
            return(f"the BMI is : {calculate_BMI()} the result is : overweight")
        else :
            return(f"the BMI is : {calculate_BMI()} the result is : fat")    
def min_BMI () :
    BMI = calculate_BMI()
    girl = age_min_girl()
    boy = age_min_boy()
    if boy == 1 :
        if BMI < 18.7 :
            return(f"the BMI is : {calculate_BMI()} the result is : underweight")
        elif 18.7 < BMI < 22.2 :
            return(f"the BMI is : {calculate_BMI()} the result is : healthy weight")
        elif 22.2 < BMI < 24.7 :
            return(f"the BMI is : {calculate_BMI()} the result is : overweight")
        else :
            return("fat") 
    elif girl == 2 :
        if BMI < 18.3 :
            return(f"the BMI is : {calculate_BMI()} the result is : underweight")
        elif 18.3 < BMI < 22.7 :
            return(f"the BMI is : {calculate_BMI()} the result is : healthy weight")
        elif 22.7 < BMI < 26.5 :
            return(f"the BMI is : {calculate_BMI()} the result is : overweight")
        else :
            return(f"the BMI is : {calculate_BMI()} the result is : fat")
def male_female () :
    age_btn.grid_forget()
    age_boy= ttk.Checkbutton(window, text="boy ", bootstyle="secondary", command=age_min_boy)
    age_boy.grid(column=0, row=5, sticky=ttk.EW, padx=10, pady=5)
    age_girl = ttk.Checkbutton(window, text='girl', bootstyle="secondary", command=age_min_girl)
    age_girl.grid(column=0, row=6, sticky=ttk.EW, padx=10, pady=5)
def answer_BMI () :
    app = ttk.Window("BMI ","solar", resizable=(False, False))
    BMI_lbl_0 = ttk.Label(app, text="BMI_Calculation")
    BMI_lbl_0.grid(columnspan=2, row=0, sticky=ttk.N, padx=20, pady=5)
    BMI_lbl = ttk.Label(app , text="")
    BMI_lbl.grid(columnspan=2, row=1, sticky=ttk.EW, padx=10, pady=5)
    age_max_answer = age_max()
    age_girl_aswer = age_min_girl()
    age_boy_answer = age_min_boy()
    if age_max_answer == 0 :
        age = age_max_BMI() 
        BMI_lbl.configure(text=age)
    elif age_girl_aswer == 2 :
        age = min_BMI
        BMI_lbl.configure(text=age)
    elif age_boy_answer == 1 :
        age = min_BMI
        BMI_lbl.configure(text=age)
#window---------------
window = ttk.Window("BMI ","solar", resizable=(False, False))
BMI_lbl_1 = ttk.Label(window, text="BMI_Calculation")
BMI_lbl_1.grid(columnspan=2, row=0, sticky=ttk.N, padx=20, pady=5)
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
age_btn= ttk.Checkbutton(window, text="age > 19 ", bootstyle="secondary", command=age_max)
age_btn.grid(column=0, row=3, sticky=ttk.EW, padx=10, pady=5)
age_btn_1 = ttk.Checkbutton(window, text='age < 19 ', bootstyle="secondary",command=male_female )
age_btn_1.grid(column=0, row=4, sticky=ttk.EW, padx=10, pady=5)
#answer-----------------
submit_btn = ttk.Button(window, bootstyle="danger" , text="answer", command=answer_BMI)
submit_btn.grid(columnspan=2, row=7, sticky=ttk.EW, padx=10, pady=5)
window.mainloop()