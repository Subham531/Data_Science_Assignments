# Exercise 3: Student Marks Processor
# This program reads student marks from a file, calculates overall marks,
# assigns grades, sorts students, writes results to an output file,
# and displays grade statistics.

# Task 1: Reads student marks data from a file (registration number, exam mark, coursework mark)


import numpy as np

# Task 3: Assigns grades based on specific rules

# Function to assign grade based on overall mark
def assigns_grade(overall):
    # Grade rules (you can adjust if institute specifies different rules)
    if overall >= 80:
        return 'A'
    if overall >= 70:
        return 'B'
    if overall >= 60:
        return 'C'
    if overall >= 50:
        return 'D'
    else:
        return 'F'

# Task 2: Computes overall marks using given weighting

# Main processing function
def mark_process():
    try:
        # Input and output file names
        input_file = "Student_in.txt"
        output_file = "Student_out.txt"

        # Lists to store student data
        student = []

        # Opening input file in read mode
        with open(input_file,'r') as f:
            # Reading each line from the file
            for line in f:
                # Spliting line into components
                reg_no,marks,course_mark = line.strip().split(',')

                # Converting marks to float
                marks = float(marks)
                course_mark = float(marks)

                # Calculate overall mark (70% exam, 30% coursework)
                overall = (0.7 * marks) + (0.3 * course_mark)

                # assigning the grade
                grade = assigns_grade(overall)

                # storing the result in the list
                student.append((reg_no, marks, course_mark,overall,grade))
        
        # Task 4: Creates a structured NumPy array

        # Creating a structured NumPy array
        dtype = [('reg_no', 'U10'), ('marks', 'f4'), ('course_mark', 'f4'), ('overall', 'f4'), ('grade', 'U1')]
        student_array = np.array(student, dtype=dtype)


        # Task 5:Sorts students by overall mark 

        # Sorting students by overall marks (descending)
        sorted_students = np.sort(student_array, order='overall')[::-1]


        # Task 6: Writes results to an output file

        # Writing results to output file
        with open(output_file,'w') as out:
            out.write('reg_no,marks,course_mark,overall,grade\n')
            for s in sorted_students:
                out.write(f"{s['reg_no']},{s['marks']},{s['course_mark']},{s['overall']:.2f},{s['grade']}\n")
            
        
        #Task 7: Display grade statistics

        print("Grade Statistics:")
        grades = ['A', 'B', 'C', 'D', 'F'] # all the grades are stored here
        for g in grades:
            count = np.sum(sorted_students['grade'] == g)
        print(f"Grade {g}: {count} students")

        #  printing the results 
        print("\nProcessing completed successfully.")
        print(f"Results saved in '{output_file}'")

    # Task 8: Handles all errors gracefully
    except FileNotFoundError:
    # Handle missing input file
        print("Input file not found. Please ensure 'students_input.txt' exists.")


    except ValueError:
    # Handle conversion errors
        print("Invalid data format in input file. Please check marks.")


    except Exception as e:
    # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")




# Call the function
mark_process()