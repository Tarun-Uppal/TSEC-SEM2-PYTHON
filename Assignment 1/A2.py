print("Enter principal amount:", end=" ")
P = float(input())
print("Enter rate of interest (in %):", end=" ")
R = float(input())
print("Enter time period (in years):", end=" ")
T = float(input())
SI = (P * R * T) / 100
print("Simple Interest is: " + str(SI))
