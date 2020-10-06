grades = [[10,25,13,45],[205], [70,75,49,100]]

def printList2D(list2D):
    for i in range(len(list2D)):
        for j in range(len(list2D[i])):
            print(list2D[i][j],end=" ")
        print()

printList2D(grades)

#caleb's version
def print_2D(grades):
    for inner_list in grades:
        for grade in inner_list:
            print(grade, end=" ")
        print()

print_2D(grades)