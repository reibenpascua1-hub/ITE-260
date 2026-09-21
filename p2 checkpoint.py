num=int(input("How many students?: "))
def grades(average):

    if  average >=90:
        print("Status: Excellent")

    elif average  >= 80:
        print("Status: Very Good")

    elif average  >= 75:
        print("Status: Passed")

    else:
        print("status: Failed")

for i in range(1,4):
    print()
    student=str(input("Enter name: "))
    activity1 = float(input("Enter Activity 1: "))
    activity2 = float(input("Enter Activity 2: "))
    activity3 = float(input("Enter Activity 3: "))
    average = (activity1 + activity2 + activity3 )/3
    print()
    print("Average:", average)

    grades(average)
    print()





