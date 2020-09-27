strings = ['a','A','abc','ABC','aBc','aBC','Abc']
#sorts with preference for capital letters
strings.sort()
print(strings) 

#to make lowercase and uppercase with same degree
#of importance->
strings = ['a','A','abc','ABC','aBc','aBC','Abc']
strings.sort(key=str.lower) #uses a function
print(strings)