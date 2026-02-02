# Set operations for different exam courses

# Define sets of students for each exam
jee_students = {"Aarav", "Siddhant", "Vedant", "Chaitanya"}
cet_students = {"Siddhant", "Vedant", "Chaitanya", "Vikram"}
neet_students = {"Rohan", "Aarav", "Chaitanya", "Yuvraj"}

print(f"JEE Students: {jee_students}")
print(f"CET Students: {cet_students}")
print(f"NEET Students: {neet_students}")

(f"JEE union CET: {jee_students.union(cet_students)}")
print(f"JEE union NEET: {jee_students.union(neet_students)}")
print(f"CET union NEET: {cet_students.union(neet_students)}")

print(f"JEE intersection CET: {jee_students.intersection(cet_students)}")
print(f"JEE intersection NEET: {jee_students.intersection(neet_students)}")
print(f"CET intersection NEET: {cet_students.intersection(neet_students)}")

print(f"JEE - CET: {jee_students.difference(cet_students)}")
print(f"NEET - CET: {neet_students.difference(cet_students)}")
print(f"CET - JEE: {cet_students.difference(jee_students)}")