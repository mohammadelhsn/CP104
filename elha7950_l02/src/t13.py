"""
-------------------------------------------------------
Lab 2, Task 13

Description:
    The final grade for a course is based upon a midterm and an exam. 
    The midterm is worth 35% of the course grade, and the exam is worth 65% 
    of the course grade. Given these weightings (use as constants) and the marks 
    on the midterm and exam, calculate the final grade for a student. 
    Print one decimal for the final grade.
-------------------------------------------------------
Author:  Mohammad El-Hassan
ID:      169067950
Email:   elha7950@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Get the user input

midterm_mark = float(input("Midterm mark (%): "))
exam_mark = float(input("Exam mark (%): "))

# Define Constants

MIDTERM_WEIGHT = 0.35
EXAM_WEIGHT = 0.65

# Calculations

FINAL_GRADE = round((midterm_mark * MIDTERM_WEIGHT) +
                    (exam_mark * EXAM_WEIGHT), 1)

# Output results

print(f"\nFinal Grade (%): {FINAL_GRADE}")
