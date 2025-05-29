std_num = int(input("Enter the number of students: "))

for i in range(std_num):
    name = input("Enter the name of the student: ")
    score = int(input("Enter the score of the student: "))
    if score >= 80:
        print(f"{name} got A")
    elif score >= 70:
        print(f"{name} got B")
    elif score >= 60:
        print(f"{name} got C")
    elif score >= 50:
        print(f"{name} got D")
    else:
        print(f"{name} got F")
