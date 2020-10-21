try:
    file = open("input.txt",'r')
    #an exception is an error that shows up in the terminal
    int(file.read()) # it's gonna cause an exception
except FileNotFoundError as e:
    print("cannot find file")
except Exception as e: #e is an exception
    print("something went wrong")
finally:
    print("allways")
    #this one is allways done in case program 'explodes'
    file.close()

#there are different types of exceptions