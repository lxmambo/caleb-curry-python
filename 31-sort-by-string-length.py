strings = ['a','A','abc','ABC','HELLO','aBc','aBC','Abc']
strings.sort(key=len)
print(strings)

#another option using key inside sorted
strings = ['a','A','abc','ABC','HELLO','aBc','aBC','Abc']
print(sorted(strings, key=len))