##Write a program that prints the numbers from 1 to 100. 
##But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
##For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1, 101):
	if num % 15 == 0:
		print"FizzBuzz"
	elif num % 5 == 0:
		print "Buzz"
	elif num % 3 == 0:
		print "Fizz"
	else:  
		print num
def fizzbuzz(n):
	print 'n in Fizzbuzz function', n
	return 'Fizz'

testvalues = {3:'Fizz', 5:'Buzz', 15:'FizzBuzz'}
print 'GOCOLTS*********************'

for k in testvalues:
	print k
	print 'testvalue should be:',testvalues[k]  
	print 'fizzbuzz output:', fizzbuzz(k)
	assert testvalues[k] ==  fizzbuzz(k)
	
	