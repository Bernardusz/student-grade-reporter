from allfunctions import completedata, listofstudent, read_students, read_grades, write_report, input_data
import time
if __name__ == "__main__":
    userinput = input("Do you want to input anything ? : ")
    if userinput in ["yes", "ye", "y"]:
        userinput1 = int(input("How many data ?"))
        for i in range(userinput1):
            name = input("Enter his/her name : ")
            science = int(input("Enter his/her science grade : "))
            english = int(input("Enter his/her english grade : "))
            math = int(input("Enter his/her math grade : "))
            input_data(name, math, english, science)

        print("Done !, processing name...")
        time.sleep(3)

        read_students("students.txt")

        print("Finished processing name ! Processing grades...")
        time.sleep(3)

        read_grades("grades.csv")

        print("Finished processing grade ! Processing to make a report..")
        time.sleep(3)

        write_report("report.json", completedata)
        print("Finished ! you now may look at report.json !")
    elif userinput in ["nope", "nop", "no", "n"]:
        print("Done ! Processing name...")
        time.sleep(3)

        read_students("students.txt")

        print("Finished processing name ! Processing grades...")
        time.sleep(3)

        read_grades("grades.csv")

        print("Finished processing grade ! Processing to make a report..")
        time.sleep(3)

        write_report("report.json", completedata)
        print("Finished ! you now may look at report.json !")
    
    else:
        print("I'll take that as a no")
        print("Done ! Processing name...")
        time.sleep(3)

        read_students("students.txt")

        print("Finished processing name ! Processing grades...")
        time.sleep(3)

        read_grades("grades.csv")

        print("Finished processing grade ! Processing to make a report..")
        time.sleep(3)

        write_report("report.json", completedata)
        print("Finished ! you now may look at report.json !")

            