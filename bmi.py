def calculate_bmi(height,weight):
    print("height = " + str(height))
    print("weight = " + str(weight))

    bmi = weight / height**2

    print("bmi = " + str(round(bmi,2)))

    if bmi<18.5:
        print("Under weight")
        return -1
    elif bmi>= 18.5 and bmi<= 25.0:
        print("normal weight")
        return 0
    else:
        print("Overweight")
        return 1

calculate_bmi(weight=50,height=1.73)