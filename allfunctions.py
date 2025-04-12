import csv
import json

listofstudent = []
completedata = {}

def read_students(file_path):
    with open(file_path, "r") as f:
        readertxt = f.readlines() #Already has list of students
        for student in readertxt:
            listofstudent.append(student.strip())

def read_grades(file_path):

    with open(file_path,"r") as f:
        readercsv = csv.DictReader(f)
        for row in readercsv:
            if row["name"] in listofstudent:
                averagegrades = (int(row["science"]) + int(row["english"])  + int(row["math"])) / 3
                completedata[row["name"]] = {
                    "absence": True,
                    "math": int(row["math"]),
                    "english": int(row["english"]),
                    "science": int(row["science"]),
                    "averagegrade": int(averagegrades)
                }


        for student in listofstudent:
            if student not in completedata:
                completedata[student] = {
                    "absence": False
                }

                
def write_report(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

def input_data(name, math, english, science):
    with open("students.txt", "a", newline="") as f:
        f.writelines(f"\n{name}")

    with open("grades.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, math, english, science])
    print("Added !")