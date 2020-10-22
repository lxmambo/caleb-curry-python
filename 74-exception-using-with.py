#automatically close files after opening them
#if an exception occurs will not be necessary 
#to close the file in a finally block

with open("input.txt") as file:
    if not file.closed:
        print("open")
    #open the file that doesn't exist can cause an error
if file.closed:
    print("closed")

try:
    file2 = open("input.txt")
except OSError:
    print("cannot open!")
else: #executes if we don't have problems opening
    with file:
        #code to parse the file
        print(file.readline())