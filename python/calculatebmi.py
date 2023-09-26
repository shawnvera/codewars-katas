# Begin
# Argument input = weight and height
# Formula for calculation is BMI = weight / height ** 2
# Condtional if below 18.5 == "underweight", 
# if below 25 == "Normal", if below/equal to 30 == "Overweight", if over 30 == "Obese"
# Return answer
# End

def bmi(weight, height):
    # BMI formula set to a variable
    bmi = weight / (height ** 2)
    
    # Conditional if checking value of BMI and returning appropriate response.
    if(bmi <= 18.5):
        return "Underweight"
    elif(bmi <= 25):
        return "Normal"
    elif(bmi <= 30):
        return "Overweight"
    else:
        return "Obese"