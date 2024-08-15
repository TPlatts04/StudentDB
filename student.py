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
    options = input("Would you like to add a student or read from the file? (A/R): ").upper()
    if options == "R":
        f = open(FILENAME, "r")
        line = f.readlines()
        if len(line) > 1:
            i = 1
            while i < len(line):
                print(line[i].replace(",", " ").strip())
                i += 1
            sys.exit()
        else:
            print("Can't read from file as there is no students...")
            main()
    studentName = input("What is the students name? ").capitalize()
    studentAge = int(input("What is the students age? "))
    studentBestSubject = input("What is the students best performing subject? ").capitalize()
    studentInstance = Student(studentName, studentAge, studentBestSubject)
    return studentInstance, csvFieldnameAssignment(studentInstance)


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

if __name__ == "__main__":
    if os.path.isfile(FILENAME):
        ...
    else:
        f = open(FILENAME, "w")
        f.write("name,age,bestSubject\n")
        f.close()
    main()