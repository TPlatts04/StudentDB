import csv, os

FILENAME = "student.csv"

def main():
    print("Test")

if __name__ == "__main__":
    if os.path.isfile(FILENAME):
        ...
    else:
        f = open(FILENAME, "w") 
        f.close()
    main()