
def solution(S):
	# convert string Binary to int Decimal
	decimal_ = int(S,2)

	# call function to get the required steps
	steps = step_count(decimal_)

	# return value
	return(steps)

def step_count(V):
	# set the initial counter to zero
	counter = 0

	# start a whileloop, and run it until V becomes Zero
	while V != 0:
		# use the logic. if odd subtract 1, if even divide by 2
		V = V - 1 if V%2==1 else V/2
		# print(V)
		# increment the counter
		counter = counter + 1
	# if V turns zero, return the counter
	return(counter)

if __name__ == '__main__':
	number = "011100"
	print(solution(number))
