# Given the names and grades for each student in a class of  students, store them in a 
# nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Print the name(s) of any student(s) having the second lowest grade in. 
# If there are multiple students, order their names alphabetically and print each one on a new line.

std_data = []
n = int(input())

# accept name and grade

for i in range(n):
    name = input()
    grade = float(input())
    std_data.append([name,grade])
    
std_set = set()
for i in range(n):
    std_set.add(std_data[i][1])
    
stdList = list(std_set)
stdList.sort()
grade_list = []

# Fetching data of student whoes marks are same as 2nd lowest student

for i in range(n):
    if stdList[1] ==  std_data[i][1]:
        grade_list.append(std_data[i])
grade_list.sort()
for i in range(len(grade_list)):
    print(grade_list[i][0])

