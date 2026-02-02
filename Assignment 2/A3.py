students = {}

while True:
    print("\n--- Student Records Management ---")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - View All Students")
    print("4 - View Specific Student")
    print("5 - Delete Student")
    print("6 - Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        
        if roll_no in students:
            print("Student already exists!")
        else:
            name = input("Enter Name: ")
            math_grade = float(input("Enter Math grade: "))
            english_grade = float(input("Enter English grade: "))
            science_grade = float(input("Enter Science grade: "))
            attendance = float(input("Enter Attendance percentage: "))
            
            grades = {
                "Math": math_grade,
                "English": english_grade,
                "Science": science_grade
            }
            
            students[roll_no] = {
                "name": name,
                "grades": grades,
                "attendance": attendance
            }
            
            print("Student added successfully!")
    
    elif choice == "2":
        roll_no = input("Enter Roll Number to update: ")
        
        if roll_no not in students:
            print("Student not found!")
        else:
            print("\nWhat do you want to update?")
            print("1. Grades")
            print("2. Attendance")
            
            update_choice = input("Enter choice (1-2): ")
            
            if update_choice == "1":
                subject = input("Enter subject (Math/English/Science): ")
                new_grade = float(input(f"Enter new {subject} grade: "))
                students[roll_no]["grades"][subject] = new_grade
                print("Grade updated!")
                
            elif update_choice == "2":
                new_attendance = float(input("Enter new attendance: "))
                students[roll_no]["attendance"] = new_attendance
                print("Attendance updated!")
    
    elif choice == "3":
        if not students:
            print("No students in records!")
        else:
            print("\n--- All Students ---")
            for roll, details in students.items():
                print(f"\nRoll No: {roll}")
                print(f"Name: {details['name']}")
                print(f"Grades: {details['grades']}")
                print(f"Attendance: {details['attendance']}%")
    
    elif choice == "4":
        roll_no = input("Enter Roll Number: ")
        
        if roll_no not in students:
            print("Student not found!")
        else:
            details = students[roll_no]
            print(f"\n--- Student Details ---")
            print(f"Roll No: {roll_no}")
            print(f"Name: {details['name']}")
            print(f"Grades: {details['grades']}")
            print(f"Attendance: {details['attendance']}%")
    
    elif choice == "5":
        roll_no = input("Enter Roll Number to delete: ")
        
        if roll_no not in students:
            print("Student not found!")
        else:
            del students[roll_no]
            print("Student deleted successfully!")
    
    elif choice == "6":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please try again.")
