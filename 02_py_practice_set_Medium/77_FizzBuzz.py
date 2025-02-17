'''
7. FizzBuzz
Print numbers from 1 to 100. But for multiples of 3 print “Fizz” instead of the number and for the multiples of 5 print “Buzz”. For numbers that are multiples of both 3 and 5 print “FizzBuzz”.

''' 
start = 1
end = 100
for x in range(start,end):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
        
