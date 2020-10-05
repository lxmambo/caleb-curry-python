grades = [[10,25,13,45],[205], [70,75,49,100]]
print(grades[2])

grades[1].append(70)
print(grades[1])
print(grades[1][1])

for inner_list in grades:
    print(inner_list)

for inner_list in grades:
    for grade in inner_list:
        print(grade, end=" ") #what is this syntax? end the print with a 
                              #whit space?
    print()

for i in range(len(grades)):
    for j in range(len(grades[i])):
        print(grades[i][j], end=" ")
    print() #to create a new linte