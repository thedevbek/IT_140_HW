
## input employee's name
## input number of hours employee worked
employee_name = input("Please input employee's name: ")
hours_worked = int(input("Please input number of hours employee worked: "))
## if hours_worked < 40 calculate regular_pay by hours_worked * 20
## Then print out statement of regular pay
if hours_worked < 40:
    regular_pay = hours_worked * 20
    print(f'Regular pay is {regular_pay}')
## if hours_worked > 40 get the regular pay, calculate the remain overtime hours * 30 
## Then print out final statement with overtime_pay as well. 
elif hours_worked > 40:
    regular_pay = 800
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * 30
    print(f'Regular pay is {regular_pay} and overtime pay is {overtime_pay} giving a total of {regular_pay + overtime_pay}')
    