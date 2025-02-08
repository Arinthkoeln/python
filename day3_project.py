#output : Regina George earned $800 this week.

name = input("Enter the employee name:").strip().title()
hourly_wage = input("enter the hourly_wage:")
work_hour = input("enter the working hour:" )
total_amount = float(hourly_wage) *float( work_hour)

print(f"{name} earned ${total_amount} this week")
