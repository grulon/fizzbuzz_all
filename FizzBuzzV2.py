import sys

def fizzbuzz(n):
	"This calcs Mod 3, 5, 15 on number passed to it and determines if Fizz, Buzz, Fizzbuzz, or blank is returned"
	
	if n % 15 == 0:
		return 'FizzBuzz'
	elif n % 5 == 0:
		return 'Buzz'
	elif n % 3 == 0:
		return 'Fizz'
	else:
		return n

def getinput()	:
	var = 0
	var = raw_input("Please enter a number: ")
	try:
		var = int(var)
		return var
	except:
		var = getinput()
		return var
	
x = sys.argv[1]

try:
	x = int(x)
except:
	print 'You didn''t pass in a number, please try again: '
	x = int(getinput())
finally:
	print fizzbuzz(x)
	
	
"""  
# used for Function testing
testvalues = {3:'Fizz', 5:'Buzz', 15:'FizzBuzz'}

for k in testvalues:
	print k
	print 'testvalue should be:',testvalues[k]
	print 'fizzbuzz output:', fizzbuzz(k)
	assert testvalues[k] ==  fizzbuzz(k)
"""
