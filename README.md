# Student Grades Processor

This Python project processes student grades by reading data from a `.txt` file containing student names, a `.csv` file containing grades, and generates a final report in `.json` format. The script calculates average grades and marks students as "missing" if they don't have grades.

## Project Structure

- `students.txt` - A text file containing student names (one per line).
- `grades.csv` - A CSV file with columns: name, math, english, science.
- `report.json` - The generated JSON report with student grades and averages.

## Features

- Reads student names from `students.txt`.
- Reads and matches grades from `grades.csv`.
- Calculates the average grade for each student.
- Generates a JSON report with the grades and average.
- Option to add new student data via the script.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Bernardusz/student-grade-reporter.git
2. Install the requirement
   pip install -r requirements.txt
3. Run the script
   python main.py
