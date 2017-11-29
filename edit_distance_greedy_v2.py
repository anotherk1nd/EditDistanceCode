
def GreditDist(str1, str2):
	"""This algorithm outputs the Levenshtein edit distance in a greedy way and shows step by step how str1 turns into str2
	For this, it takes in account the previous and next characters of the current letter"""
	
	m = len(str1) #Length of str1
	n = len(str2) #Length of str2
	c1 = c2 = 1 #cursor on str1, cursor on str2
	result_string = ""
	result_c = 1 #cursor on the result string
	min_mn = min(m, n) #minimum between m and n
	edit_distance = 0 #edit distance
	
	
	#For more convenience, I swap of str2 is shorter than str1 (you will understand why)
	if (min_mn == n):
		str1, str2 = str2, str1
		m,n = n, m
	
	
	print("Transforming ",str1," into ",str2,"...")
	#I do a comparison two by two of the characters over the length of the shortest string
	#For the method I'm about to provide, it's likely to take less time than the other way around
	for i in range(min_mn):
		#Print the result string
		print(str1)
		print(str2)
		print("State: ",result_string)
		print("----------------------\n")
		
		
		
		#test if both current characters are the same
		if str1[c1] == str2[c2]:
			#In this case, I do nothing and I move on
			c1 += 1
			c2 += 1
			result_string = result_string + str1[c1]
			result_c += 1
		
		else:
			#increment edit distance
			edit_distance += 1
			
			#I compare the current character of str1 to the next character of str2
			if str1[c1] == str2[c2 + 1]:
				
				#They are the same, the best at this moment is to insert the current character on str2 before the current one of str1
				if (result_c == 1)
					result_string = str2[c2] + result_string[result_c - 1:]
				else:
					result_string = result_string[:result_c - 1] + str2[c2] + result_string[result_c - 1:]
					
				
				c1 += 1
				c2 += 2
					
			
			#Else, if the next character on str1 and the current character of str2 are alike then I need to delete the current character on str1
			#I can do that since all the previous characters on both strings till now are the same
			
			elif c1 < min_mn: #if it's the end of the first string, no deletion possible
			
				if str1[c1 + 1] == str2[c2]:
					result_string += str2[c2]
					c1 += 2
					c2 += 1
				
				
			#Else, substitution is my backup solution... str1[c1] becomes str2[c2]
			else:
				result_string += str2[c2]
				c1 += 1
				c2 += 1
			
	#If there are remaining characters, I insert/delete them to the result string
	if min_mn < n:
		for j in intervalle(i, n+1):
			result_string += str2[j]
	#edit distance += length(str2) - length(result string)
	edit_distance += n - len(result_string)
	
	
	return int(edit_distance)