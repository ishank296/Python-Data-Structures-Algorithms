'''
Rolling Hashing Algorithm
Rabin Karp algorithm matches the hash value of the pattern with the hash value of current substring of text, 
and if the hash values match then only it starts matching individual characters. 
So Rabin Karp algorithm needs to calculate hash values for following strings.

1) Pattern itself.
2) All the substrings of text of length m.
'''


# d is the number of characters in the input alphabet
# q  a random prime number
d = 256
def pattern_search(text,pattern,q):
	M = len(pattern)
	N = len(text)
	p = 0 # hash value of pattern
	t = 0 # hash value of text
	h = 1

	# The value of h would be "pow(d, M-1)%q"
	for i in xrange(M-1):
		h = (h*d)%q


	# calculate the hash value of pattern
	for i in xrange(M):
		p=(d*p + ord(pattern[i]))%q

	# calculate the hash value of text
		t=(d*t + ord(text[i]))%q

	#sliding pattern over text one by one
	for i in xrange(N-M+1):
		if p == t:
		   #check characters one by one
		   for j in xrange(M):
		   		if text[i+j]!= pattern[j]:
		   			break

		   j+=1
		   if j == M:
			   print "Pattern Found at index: " + str(i)


		# calculate hash value for next window in text
		if i < N-M:
			t = (d*(t-ord(text[i])*h) + ord(text[i+M]))%q

			# We might get negative values of t, converting it to
			# positive
			if t < 0:
				t = t+q

