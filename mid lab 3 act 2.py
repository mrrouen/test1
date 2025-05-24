def main():
    student_subjects = {}

    num_students = int(input("Enter the number of students: "))

    for _ in range(num_students):
        student_name = input("Enter student name: ")
        subjects = input(f"Enter subjects for {student_name} (comma-separated): ").split(", ")
        student_subjects[student_name] = subjects

    def display_subjects(student_name):
        if student_name in student_subjects:
            print(f"{student_name}'s Subjects: {', '.join(student_subjects[student_name])}")
        else:
            print(f"Student {student_name} not found.")

    def check_subject_enrollment(student_name, subject):
        if student_name in student_subjects:
            if subject in student_subjects[student_name]:
                print(f"Yes, {student_name} is enrolled in {subject}.")
            else:
                print(f"No, {student_name} is not enrolled in {subject}.")
        else:
            print(f"Student {student_name} not found.")
    
    student_name_to_check = input("\nEnter student name to check subjects: ")
    display_subjects(student_name_to_check)

    subject_to_check = input("\nEnter subject to check enrollment: ")
    check_subject_enrollment(student_name_to_check, subject_to_check)

main()
