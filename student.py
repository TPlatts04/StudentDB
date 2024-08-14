import csv
import os

FILENAME = "student.csv"
CSV_FIELDNAMES = []

class Student():
    def __init__(self, name, age, bestSubject) -> None:
        self.name = name
        self.age = age
        self.bestSubject = bestSubject
        

def main():
    studentName = input("What is the students name? ")
    studentAge = int(input("What is the students age? "))
    studentBestSubject = input("What is the students best performing subject? ")
    studentInstance = Student(studentName, studentAge, studentBestSubject)
    return studentInstance, csvFieldnameAssignment(studentInstance)


# Allow the amount of fieldnames to be flexible, providing the programmer adds more variabless to class etc.
def csvFieldnameAssignment(tempStudent):
    f = open(FILENAME, "r")
    line = f.readline()
    CSV_FIELDNAMES.extend((line.strip().split(",")))
    csvWriteStudent(tempStudent)


def csvWriteStudent(writeStudent):
    with open(FILENAME, "a", newline="\n") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_FIELDNAMES)
        writer.writerow({CSV_FIELDNAMES[0]: writeStudent.name, CSV_FIELDNAMES[1]: writeStudent.age, CSV_FIELDNAMES[2]: writeStudent.bestSubject})
    csvOutput()


def csvOutput():
    with open(FILENAME, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row[CSV_FIELDNAMES[0]], row[CSV_FIELDNAMES[1]], row[CSV_FIELDNAMES[2]])
    

if __name__ == "__main__":
    if os.path.isfile(FILENAME):
        ...
    else:
        f = open(FILENAME, "w")
        f.write("name,age,bestSubject\n")
        f.close()
    main()