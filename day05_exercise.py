"""list1 = [1,2,3,4]
list2 = [1,2,3,4]

if(id(list1) == id(list2)):
    print("True")
else:
    print("false") 
    
numbers1= [1, 2, 3, 4]
#new_numbers = numbers + [5]
number2 = [1,2,3,4,5,6]
numbers1.append(5)
numbers1.append("Arin")
number2.pop()
print(numbers1 == number2)

user_number = int(input("enter the value:"))


if (user_number > 0):
    print("the number is positive")
elif(user_number < 0 ): 
    print("the number is negative")   
else:
    print("number is equal to zero")"""
    
employee_name = input ("Enther the employee name:")   
userwork_hour = int(input("enter the work_hour:"))
hourly_wage = float(input("enter the hourly wage:")) 



if (userwork_hour>40) :
        print("Employe is due some additional pay, as well as the amount due")
        over_hour = userwork_hour - 40
        overtime = over_hour * hourly_wage * 1.1
        regular_pay = 40 * hourly_wage
        employee_pay = regular_pay + overtime
       
else:
    employee_pay = userwork_hour * hourly_wage
    
        

print(f"{employee_name} is  getting the payement {employee_pay} ")           
    
    
       