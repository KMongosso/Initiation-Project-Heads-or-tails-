from random import randint


def n_bits_pattern(historic,turn,n):
	#initilization of memory, the table that will count each pattern in the historic
	memory= []
	for i in range(0,2**n):
		memory.append(0)

	if turn >= n : #turn must be higher than the pattern evaluation
		#evaluation of each pattern in historic
		for k in range(n-1,turn):
			#generate a binary number in a list
			binary = []
			for b in range(0,n):
				binary.append(historic[k-n+b])

			index= convert(binary)
			memory[index] = memory[index]+1
		binary = []
		print(binary)

		#evaluation of the last pattern wich the last number is to predict
		for b in range(0,n-1):
			binary.append(historic[turn-n+b+1])


		if memory[convert(binary)*2] > memory[convert(binary)*2 + 1] :
			return 0
		else :
			return 1
	else :
		return randint(0,1)

#convert binary to decimal
def convert(binary):
	binary.reverse()
	print(binary)
	decimal = 0
	for i in range(0,len(binary)) :
		decimal = decimal + (2**i)*binary[i]
	return decimal

#test :
historic = [0,0,1,0,1,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1]
pred = []
n=3
for i in range(0,len(historic)):
	pred.append(n_bits_pattern(historic,i,n))
print(pred)


test = [0,0,1]
print(test[convert(test)])







