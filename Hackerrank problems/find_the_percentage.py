#Hackerrank problem "Find the percentage"
if __name__ == '__main__':
    n = int(input()) # number of students
    student_marks = {}  # dictionary to store the student name and marks
    for _ in range(n): # created a loop to iterate over the number of students
        name, *line = input().split() # split the name and marks of the students
        scores = list(map(float, line)) # convert the marks to float
        student_marks[name] = scores # store the name and marks in the dictionary
    query_name = input() #Input for the student name to find the average marks
if query_name in student_marks.keys(): # this if statement checks if the student name is in the dictionary or not
    avg= float(sum(student_marks[query_name]) / len(student_marks[query_name])) #this will caldulate the average marks
    print(f"{avg:.2f}") #this will print the average marks upto 2 decimal places