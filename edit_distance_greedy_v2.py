#I'm calling this the sliding lantern

def GreditDist(str1, str2):
	"""This algorithm outputs the Levenshtein edit distance in a greedy way and shows step by step how str1 turns into str2
	For this, it takes in account the previous and next characters of the current letter"""
	
	m = len(str1) #Length of str1
	n = len(str2) #Length of str2
	str1 += '0'
	str2 += '0'
	c1 = c2 = 0 #cursor on str1, cursor on str2
	result_string = "" #portion already modified of the string
	result_c = 0 #cursor on the result string
	min_mn = min(m, n) #minimum between m and n
	edit_distance = 0 #edit distance
	########## ALIGNMENT VARIABLES ########
	str1_alignment = ''
	str2_alignment = ''
	mark = ''


	if m == 0:
		str1_alignment = ''.join(['-' for i in range(n)])
		mark = ''.join([' ' for i in range(n)])
		
		return n#, str1_alignment, str2, mark #I return the edit distance and the matching alignment

	if n == 0:
		str2_alignment = ''.join(['-'for i in range(m)])
		mark = ''.join([' ' for i in range(m)])
		
		return m#, str1, str2_alignment, mark
	
	#For more convenience, I swap of str2 is shorter than str1 (you will understand why)
	if (min_mn == n):
		str1, str2 = str2, str1
		m,n = n, m
	
	
	#print("Transforming \""+str1+"\" into \""+str2+"\"...\n")
	#I do a comparison two by two of the characters over the length of the shortest string
	#For the method I'm about to provide, it's likely to take less time than the other way around
	while c1 < min_mn:
		
		#test if both current characters are the same
		if str1[c1] == str2[c2]:
			#In this case, I do nothing and I move on
			#print(result_string + str1[c1:])
			#Building up the alignment
			str1_alignment += str1[c1]
			str2_alignment += str2[c2]
			mark += '|'
			
			result_string = result_string + str1[c1]
			c1 += 1
			c2 += 1
			result_c += 1
			
		
		elif str1[c1] == str2[c2 + 1]:
			#increment edit distance
			edit_distance += 1
			
			#I compare the current character of str1 to the next character of str2

			# print("--- INSERTION ---")
			# They are the same, the best at this moment is to insert the current character on str2 before the current one of str1
			# print(result_string + str2[c2] + str1[c1:])  # evolution of str1 to str2 for insertion
			result_string = result_string + str2[c2] + str1[c1]
			# Alignment
			# str1_alignment += '-' + str1[c1]
			# str2_alignment += str2[c2] + str2[c2 + 1]
			# mark += ' ' + ' '

			c1 += 1
			c2 += 2
			result_c += 2

			# Else, if the next character on str1 and the current character of str2 are alike then I need to delete the current character on str1
			# I can do that since all the previous characters on both strings till now are the same


		elif str1[c1 + 1] == str2[c2]:  # if it's the end of the first string, no deletion possible

			# print("--- DELETION ---")

			# print(result_string + str1[c1 + 1:]) #Evolution for deletion
			edit_distance += 1

			result_string += str2[c2]

			# alignment

			# str1_alignment += str1[c1] + str1[c1 + 1]

			# str2_alignment += '-' + str2[c2]

			# mark += ' ' + ' '

			c1 += 2

			c2 += 1

			result_c += 1

		# Else, substitution is my backup solution... str1[c1] becomes str2[c2]

		else:

			# print("--- SUBSTITUTION ---")

			# print(result_string + str2[c2] + str1[c1 + 1:]) #evolution for substitution
			edit_distance += 1

			result_string += str2[c2]

			# alignment

			# str1_alignment += str1[c1]

			# str2_alignment += str2[c2]

			# mark += ' '

			c1 += 1

			c2 += 1

			result_c += 1




		# Print the result string
		# print(str2)
		# print("State: ", result_string+"_")
		# print("Cursors:",c1 + 1, c2 + 1) #Current position of the cursors
		# print("----------------------\n")

			
	#If there are remaining characters, I insert/delete them to the result string
	if c1 >= m and c2 < n:
		for j in range(c2, n):
			#print("--- BOTTOM INSERTION")
			result_string += str2[j]
			#alignment
			# str1_alignment += '-'
			# str2_alignment += str2[j]
			
			edit_distance += 1
			c1 += 1
			c2 += 1
			# Print the result string
			# print(result_string)
			# print(str2)
			# print("State: ", result_string+"_")
			# print("Cursors:",c1 + 1, c2 + 1)
			# print("----------------------\n")
	#edit distance += length(str2) - length(result string)
	#edit_distance += n - len(result_string)
	
	return edit_distance#, str1_alignment, str2_alignment, mark


###### TEST SESSION

# str1 = ""
# str2 = "saturday"
#
# edit_distance, al1, al2, mark = GreditDist(str1, str2)
#
# print("Levenshtein Edit distance (approximation):", edit_distance)
# print("************************ ALIGNMENT ***************************")
# print(al1)
# print(mark)
# print(al2)


edit = GreditDist("abcd", "decad")
print(edit)