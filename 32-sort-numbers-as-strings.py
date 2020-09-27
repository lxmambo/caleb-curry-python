numbers = [1,54,76,12,111,4343,6,8888,3,222,1,0,222,-1,-122,5,-30]
numbers_str = ['1','54','76','12','111','4343','6','8888','3','222','1','0','222','-1','-122','5','-30']
numbers2 = numbers[:]
numbers_str.sort()
print(numbers_str)

numbers2.sort(key=str) #converts numbers into a string
#equivalent to do str(5) for all numbers

print(numbers2)