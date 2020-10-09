#association between two pieces of data
#similar to an associative array, or object in javascript

emails = {
    'caleb':'caleb@email.com',
    'gal':'g@email.com',
    (5,5): 'test', #tuple -> has hash method
    #[5,5]: 'test2', #lists don't have hash method, it's a mutable type
    #strings, integers, tuples, etc are immutable, so they are ok
    }
#Key/Value

print(emails)

#objects can have an internal method called __hash__ that 
#takes the data and does some processing to converting it
#into integer

print(hash('caleb'))

#the generated integer determines where the value associated
#to that key is stored
#immutable data types are hashable, the key must have the method hash

#increasing the size of a list doesn't increase access time
#lists are different, bigger lists have bigger access times
#iteration is needed to find the data
#dictionaries are good to fast look ups and fast inserts