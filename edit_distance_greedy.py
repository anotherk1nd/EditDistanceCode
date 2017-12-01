


def GreditDist(str1, str2):
	"""This function computes and returns the approximation of the edit distance of str1 and str2
	in a greedy manner"""

	edit = 0 #edit distance, computed in an incremental way
	m = len(str1)
	n = len(str2)
	#First, we need to determine the biggest of the sequences
	longest_length = max(len(str1), len(str2))

	if m == 0:
		return n

	if n == 0:
		return m


	#If str1 and str2 have different lengths, then we probably need |m - n| insertions/deletions
	# given a childish manner to think
	import math
	edit = math.fabs(m - n)
	

	#We cross min(m,n) of both sequences and if two characters are different, then we suppose
	#a substitution is needed
	#We therefore increments edit
	min_mn = min(m, n)
	for i in range(min_mn):
		if str1[i] != str2[i]:
			edit += 1

			
	return int(edit)
