employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]


for employee in employees:
    total_pay = employee[1] * employee[2]
    print(f"{employee[0]} has to be paid £{total_pay:.2f}")


houly_total = 0
for employee_list in employees:
    
       houly_total +=  employee_list[2]
    
       #print(f"{employee_list[0]} due amount is :{due_amount}")
       
              
avarage = houly_total/len(employees)
print(avarage)       

for employee_list in employees:     
        if employee_list[2]> avarage:
           print(f"{employee_list[0]} is getting hourly wage above avarage")
           
       