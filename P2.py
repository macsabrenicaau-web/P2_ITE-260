print("STUDENT ACTIVITY SCORE SYSTEM")

Students = int(input("\nHow many students? "))

def Student():
    S_1 = (input("Enter name: "))
    A_1 = float(input("Activity 1: "))
    A_2 = float(input("Activity 2: "))
    A_3 = float(input("Activity 3: "))

    return S_1, (A_1 + A_2 + A_3) / 3

def status(Average):
    if Average >= 90:
        return "Excellent"
    elif Average >=80:
        return "Very Good"
    elif Average >= 75:
        return "Passed"
    else:
        return "Failed"

for i in range(Students):
    print("\nESTUDYANTE NI MACI:", i + 1)
    S_1, Average = Student()
    Status = status(Average)

    print("\nRESULT")
    print("Scholar ni Maci, Name:", S_1)
    print("Average:", round(Average, 2))
    print("Status:", Status)

#/n = move to the next line of code. Para di nakaka bother tignan sa out put 
#round = round off. Para di mahaba ang decimal at accurate ang out put
