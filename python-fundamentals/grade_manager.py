

#main database

""" Contains student details in nested order
    student1 (name) - subjects, scores, avg, grade
"""
db = {}

#func1
def add_student(db, name):
    if name not in db:
        db[name] = {}
        print(f"Student {name} added successfully.")
    else:
        print(f"Student {name} already exists in the database.")

def add_score(db, name, subject, score):
    if name not in db:
        print(f"Student {name} does not exist. Please add the student first.")
        return
    
    if subject not in db[subject]:
        db[name][subject] = []
    db[name][subject].append(score)
    print(f"Score {score} added for {name} in {subject}.")

def get_avg(db, name):
    if name not in db:
        print(f"Student {name} does not exist.")
        return None
    
    total_score = 0
    count = 0
    for subject, scores in db[name].items():
        total_score += sum(scores)
        count += len(scores)
    
    avg = total_score / count if count > 0 else 0
    db[name]['avg'] = avg
    return avg

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    else:
        return "C"

def top_student(db):
    top_name = None
    highest = 0
    
    for student in db:
        avg = get_avg(db, student)
        
        if avg > highest:
            highest = avg
            top_name = student
    return top_name, highest

def sub_avg(db):
    subjects = {}
    
    for student in db:
        for subject in db[student]:
            if subject not in subjects: 
                subjects[subject] = []
            
            subjects[subject].extend(db[student][subject])
            
    averages = {}
    
    for subject in subjects:
        averages[subject] = sum(subjects[subject]) / len(subjects[subject])
        
    return averages 

def students_above(db, threshold):
    result = []
    
    for student in db:
        avg = get_avg(db, student)
        
        if avg > threshold:
            result.append(student)
    return result

def generate_report(db):
    print("\n===== STUDENT REPORT =====")

    print(f"{'Name':<15}{'Average':<10}{'Grade':<10}")

    for student in db:
        avg = get_avg(db, student)
        grade = get_grade(avg)

        print(f"{student:<15}{avg:<10.2f}{grade:<10}")

    print()


#interactive loop
#user_choice = int(input("Choose an option: \n1. Add Student\n2. Add Score\n3. Generate Report\n4. Exit\n"))
while True:
    print("1. Add Student")
    print("2. Add Score")
    print("3. Generate Report")
    print("4. Top Student")
    print("5. Subject Averages")
    print("6. Students Above Threshold")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        add_student(db, name)

    elif choice == "2":
        name = input("Enter student name: ")
        subject = input("Enter subject: ")
        score = float(input("Enter score: "))

        add_score(db, name, subject, score)

    elif choice == "3":
        generate_report(db)

    elif choice == "4":
        name, avg = top_student(db)

        if name:
            print(f"Top Student: {name} ({avg:.2f})")
        else:
            print("No students found.")

    elif choice == "5":
        averages = sub_avg(db)

        print("\nSubject Averages:")
        for subject in averages:
            print(f"{subject}: {averages[subject]:.2f}")

    elif choice == "6":
        threshold = float(input("Enter threshold: "))

        result = students_above(db, threshold)

        print("Students above threshold:")
        for student in result:
            print(student)

    elif choice == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")