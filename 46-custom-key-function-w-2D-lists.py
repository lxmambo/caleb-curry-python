d = [1,50,4,6,7,30,2,-2,-5,-10,50]
grades = [[10,25,13,45],[205], [70,75,49,100]]
print(sorted(grades))
print(sorted(d,key=abs)) #without abs negative 
                         #numbers would come first
print(sorted(grades, key=sum))
#in this case sums numbers in each entry and sorts

#return a list of the averages
def avg(data):
    avg_list = []
    for item in data:
        sum = 0
        for number in item:
            sum = sum + number
        avg_list.append(sum/len(item))
    return avg_list
print(avg(grades))

#caleb's version
def avg2(data):
    return sum(data)/len(data)
print(sorted(grades,key=avg2))
#avg2 is a function that applies to a list of equal 
#size numbers
data = [1,2,3]
print(sum(data))
#sorted(list,key=function) applies function to 
#all elements of a list, element by element.
