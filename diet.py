def bmi_Calculator(weight,height):
    bmi = weight/(height/100)**2
    return round(bmi,2)

def bmr_Calculator(gender,age,weight,height):
    if gender =="Male":
        bmr = (10*weight)+(6.25*height)-(5*age)+5
        return bmr
    elif gender =="Female":
        bmr = (10*weight)+(6.25*height)-(5*age)-161
        return bmr


def Tdee_calculator(bmr,Activity):#total daily energy expenditure
    activity_Factor = {"Sedentary":1.20,
                      "Lightly_Active":1.375,
                      "Moderately_active":1.55,
                      "Very_active":1.725,
                      "Extra_active":1.90
                    }
    tdee = bmr*activity_Factor[Activity]
    return round(tdee,2)

def Calories_Target(tdee,aim):
    if aim =="Weight_maintain":
        calorie =tdee
    elif aim =="Weight_loss":
        calorie = (tdee - 400)
    elif aim == "Weight_gain":
        calorie = (tdee + 300)
    return round(calorie,2)


# bmr= bmi_Calculator(60,150)
# print (bmr_Calculator("Male",25,50,150))
# tdee = (Tdee_calculator(bmr,"Very_active"))
# print(Calories_Target(tdee,"Weight_gain"))



