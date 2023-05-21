# Sequential execution
name = input("Enter employee name: ")
position = input("Enter employee position - 'L' for Lecturer and 'C' for Clerk: \n")
basic_sal = int(input("Enter employee salary: "))
ot_rate = 12

if position == "L":
    position = "Lecturer"
    allowance = int(input("Enter allowance: "))
    salary = basic_sal + allowance

else:
    position = "Clerk"
    ot_hours = int(input("Enter number of OT hours"))
    salary = basic_sal + (ot_hours * ot_rate)

print(f'{name:10} ==> {position:10} ==> {salary:10}')
