print("Please enter your basic salary: ", end="")
basic_salary = float(input())
DA = basic_salary * 0.70
TA = basic_salary * 0.30
HRA = basic_salary * 0.10
print("Dearness Allowance (DA): " + str(DA))
print("Travel Allowance (TA): " + str(TA))
print("House Rent Allowance (HRA): " + str(HRA))
print("Gross Salary: " + str(basic_salary + DA + TA + HRA))