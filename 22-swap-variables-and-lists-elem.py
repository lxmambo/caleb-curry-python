data = ["a","b","c","d","e","f","g","h"]

me = "caleb"
you = "subscriber"

print(me,you)
me, you = you, me
print(me, you)

temp = me
me = you
you = temp
print(me,you)

index = 1

print(data[index],data[-index-1])
data[index],data[-index-1]=data[-index-1],data[index]
print(data)