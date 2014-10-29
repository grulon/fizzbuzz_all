def fizzbuzz(n):
	print 'n in Fizzbuzz function', n
	if n % 15 == 0:
		return 'FizzBuzz'
	elif n % 5 == 0:
		return 'Buzz'
	elif n % 3 == 0:
		return 'Fizz'
	else:  
		return ''


testvalues = {3:'Fizz', 5:'Buzz', 15:'FizzBuzz'}
print 'GOCOLTS*********************'

for k in testvalues:
	print k
	print 'testvalue should be:',testvalues[k]  
	print 'fizzbuzz output:', fizzbuzz(k)
	assert testvalues[k] ==  fizzbuzz(k)
	
	