import ttkbootstrap as ttk
from ttkbootstrap.dialogs.dialogs import Messagebox
class calculate_BMI:
    def __init__(self,height_int,weight_int) -> float :
        self.height_cm = height_int
        self.width = weight_int

    def calculate_height(self) -> float:
        self.height_m = self.height_cm/100
        return self. height_m
    
    def calculate_bmi(self) -> float:
        return(round(self.width/self.height_m**2 , 2))
class min_boy_BMI(calculate_BMI) :

    def __init__(self, height_int, weight_int) -> float:
        super().__init__(height_int, weight_int)
        self.BMI = super().calculate_bmi()
      
    def BMI_boy (self) :
        if self.BMI< 18.7 :
            return(f"the BMI is : {calculate_BMI()} the result is : underweight")
        elif 18.7 < self.BMI < 22.2 :
            return(f"the BMI is : {calculate_BMI()} the result is : healthy weight")
        elif 22.2 < self.BMI < 24.7 :
            return(f"the BMI is : {calculate_BMI()} the result is : overweight")
        else :
            return("fat") 
class min_girl_BMI(calculate_BMI) :

    def __init__(self, height_int, weight_int) -> float:
        super().__init__(height_int, weight_int)
        self.BMI = super().calculate_bmi()
      
    def BMI_girl (self) :
        if self.BMI< 18.3 :
            return(f"the BMI is : {calculate_BMI()} the result is : underweight")
        elif 18.7 < self.BMI < 22.7 :
            return(f"the BMI is : {calculate_BMI()} the result is : healthy weight")
        elif 22.2 < self.BMI < 29.9 :
            return(f"the BMI is : {calculate_BMI()} the result is : overweight")
        else :
            return("fat")
class max_BMI(calculate_BMI) :
    def __init__(self, height_int, weight_int) -> float:
        super().__init__(height_int, weight_int)
        self.BMI = super().calculate_bmi()
      
    def BMI_max (self) :
        if self.BMI< 18.5 :
            return(f"the BMI is : {calculate_BMI()} the result is : underweight")
        elif 18.7 < self.BMI < 24.5 :
            return(f"the BMI is : {calculate_BMI()} the result is : healthy weight")
        elif 22.2 < self.BMI < 24.7 :
            return(f"the BMI is : {calculate_BMI()} the result is : overweight")
        else :
            return("fat")        
class Interface_1(ttk.Window , answer): 
    def __init__(self):
        super().__init__()
        BMI_lbl_1 = ttk.Label(text="BMI_Calculation")
        BMI_lbl_1.grid(columnspan=2, row=0, sticky=ttk.N, padx=20, pady=5)
        #height---------------
        height_lbl = ttk.Label(text="height(cm) : ")
        height_lbl.grid(column=0, row=1, sticky=ttk.W, padx=10, pady=5)
        height_int =ttk.Entry(bootstyle="success", text="Example : 170 cm")
        height_int.grid(column=1, row=1, sticky=ttk.W, padx=10, pady=5)
        #weight----------------
        weight_lbl = ttk.Label(text="weight(kg) : ")
        weight_lbl.grid(column=0, row=2, sticky=ttk.W, padx=10, pady=5)
        weight_int = ttk.Entry(bootstyle="success", text="Example : 45 kg" )
        weight_int.grid(column=1, row=2, sticky=ttk.W, padx=10, pady=5)
        #answer-----------------
        submit_btn = ttk.Button(bootstyle="danger" , text="answer" , command= answer)
        submit_btn.grid(columnspan=2, row=6, sticky=ttk.EW, padx=10, pady=5)
        #age--------------------
        self.adult_bmi = ttk.BooleanVar()
        self.adult_bmi.set(True)
        self.age_period = ttk.Radiobutton(self,
                                          text = "بازه سنی 19 سال به بالا",
                                          value = True,
                                          variable = self.adult_bmi,
                                          command= self.age_period_result)
        self.age_period.grid(column=0, row=3, sticky=ttk.EW, padx=10, pady=5)
        self.age_period = ttk.Radiobutton(self,
                                          text = "بازه سنی کمتر از 19 سال",
                                          value = False,
                                          variable = self.adult_bmi,
                                          command= self.age_period_result)
        self.age_period.grid(column=0, row=4, sticky=ttk.EW, padx=10, pady=5)
    def age_period_result(self):
        if self.adult_bmi.get():
            return True
        else:
            self.bmi = ttk.IntVar()
            self.bmi.set(0)
            self.age_period = ttk.Radiobutton(self,
                                            text ='دختر',
                                            value = 0,
                                            variable = self.bmi,
                                            command= self.age_period_result)
            self.age_period.grid(column=0, row=3, sticky=ttk.EW, padx=10, pady=5)
            self.age_period = ttk.Radiobutton(self,
                                            text ='پسر',
                                            value = 1,
                                            variable = self.bmi,
                                            command= self.age_period_result)
            self.age_period.grid(column=0, row=4, sticky=ttk.EW, padx=10, pady=5)
        def age_period_result(self):
            
            if self.bmi.get() == 0 :  
                return 0
            else:
                return 1
class answer (calculate_BMI , min_girl_BMI , min_boy_BMI , max_BMI) :
        def __init__(self, height_int, weight_int) -> float:
            super().__init__(height_int, weight_int)
        def answer (self) :
            self.adult_bmi = True
            self.bmi = 0
            if self.adult_bmi == True :
                return max_BMI
            else :
                if self.bmi == 0 :
                    return min_girl_BMI
                else :
                    return min_boy_BMI








app = Interface_1()
app.mainloop()