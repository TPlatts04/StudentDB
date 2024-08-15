import csv
import os
import sys

FILENAME = "student.csv"
CSV_FIELDNAMES = []

class Student():
    def __init__(self, name, age, bestSubject) -> None:
        self.name = name
        self.age = age
        self.bestSubject = bestSubject
        

def main():
    options = input("Would you like to add a student, read from the file or delete a student? (A/R/D): ").upper()
    match options:
        case "R":
            f = open(FILENAME, "r")
            line = f.readlines()
            if len(line) > 1:
                i = 1
                while i < len(line):
                    print(line[i].replace(",", " ").strip())
                    i += 1
                main()
            else:
                print("Can't read from file as there is no students...")
                main()
        case "A":
            studentName = input("What is the students name? ").capitalize()
            studentAge = int(input("What is the students age? "))
            studentBestSubject = input("What is the students best performing subject? ").capitalize()
            studentInstance = Student(studentName, studentAge, studentBestSubject)
            return studentInstance, csvFieldnameAssignment(studentInstance)
        case "D":
            f = open(FILENAME, "r")
            lines = f.readlines()
            if len(lines) == 1:
                print("Cannot delete as there is no students...")
            else:
                deleteStudent()
        case "_":
            raise ValueError("Invalid option, please enter A/R...")


# Allow the amount of fieldnames to be flexible, providing the programmer adds more variabless to class etc.
def csvFieldnameAssignment(tempStudent):
    f = open(FILENAME, "r")
    line = f.readline()
    CSV_FIELDNAMES.extend((line.strip().split(",")))
    csvWriteStudent(tempStudent)

# Write the students name, age and best subject to the csv
def csvWriteStudent(writeStudent):
    with open(FILENAME, "a", newline="\n") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_FIELDNAMES)
        writer.writerow({CSV_FIELDNAMES[0]: writeStudent.name, CSV_FIELDNAMES[1]: writeStudent.age, CSV_FIELDNAMES[2]: writeStudent.bestSubject})
    main()

# Delete the specified student based off of line number
def deleteStudent():
    with open (FILENAME, "r") as file:
        lines = file.readlines()
        lineNum = 1
        for x in lines:
            print(f"({lineNum}): {x}")
            lineNum += 1
        studentDelete = int(input("Enter the line number you would like to delete (number in brackets): "))
        if 1 <= studentDelete - 1 < len(lines):
            del lines[studentDelete - 1]
            with open(FILENAME, 'w') as file:
                file.writelines(lines)
            print("Student deleted...")
        elif studentDelete == 1:
            print("Cannot delete headings...\n")
            deleteStudent()
        else:
            print("Line number is out of range.")
            deleteStudent()
    main()

if __name__ == "__main__":
    if os.path.isfile(FILENAME):
        ...
    else:
        f = open(FILENAME, "w")
        f.write("name,age,bestSubject\n")
        f.close()
    main()