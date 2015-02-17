def check(seq, k):
	for i in range(1, int(seq.__len__()-1)):
		if checkForAP(seq, i, k):
			return True

def checkForAP(seq, d, k):
	for i in range(0, seq.__len__()):
		first = seq[i]
		j = 0
		#print("First"+str(first))
		count = 0
		while i+j*d < seq.__len__() and j < k:
			#print(i+j*d)
			if seq[i+j*d] == first:
				count += 1
			if count == k:
				return True
			j += 1

def next(seq, k):
	seq.append(0)
	if check(seq, k) == True:
		return backtrack(seq, k)
	return seq

def backtrack(seq, k):
	seq.reverse()
	trim = seq.index(0)
	seq[trim] = 1
	seq = seq[trim:]
	seq.reverse()
	if check(seq, k) == None:
		print(seq)
		return seq
	else:
		return backtrack(seq, k)

def main():
	n = [0]
	max = 0
	while n != [1]:
		if max < n.__len__():
			max = n.__len__()
		n = next(n, 3)
	print(max+1)

main()