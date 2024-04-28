# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"

command = input()

employees_dict={}

while command != "End":
    info = command.split(" -> ")
    company = info[0]
    employee = info[1]
    if company not in employees_dict:
        employees_dict[company] = []
    if employee not in employees_dict[company]:
        employees_dict[company].append(employee)
    else:
        pass
    command = input()
for company, employees in employees_dict.items():
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")
