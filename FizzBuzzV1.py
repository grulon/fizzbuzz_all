
# hard coded upper limit

x = 100

print 'FizzBuzz counting up to', x
for num in range(1,x+1):
	if num % 15 == 0:
		print"FizzBuzz"
	elif num % 5 == 0:
		print "Buzz"
	elif num % 3 == 0:
		print "Fizz"
	else:  
		print num
	
