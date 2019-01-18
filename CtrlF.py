import sys
from time import time
word_input = input("")
data = input("")
# data = open("text.txt","r").readlines()	
result = 0
sys.setrecursionlimit(300000)

#KMP
def recurringChar(word):
	ref = []
	patt = []
	for i in range(len(word)):
		#Added Code
		ref.append(0) 	
		if(word[i] not in patt):

			#Original Code 
			# ref.append(0) 
				
			#Replacement code
			ref[i] = 0 	
			
			patt.append(word[i])
		elif(word[i] in patt):
			
			#Original Code
			# ref.append(patt[::-1].index(word[i])+1) 
			
			#Replacement code
			ref[i] = len(ref)-(patt[::-1].index(word[i])+1) 
			
			patt.append(word[i])
		# print(ref)
	return ref

def changed_recurringChar(word):
	ref = [0]
	patt = [0]
	for i in range(len(word)):
		if(word[i] not in patt):
			patt.append(word[i])
			ref.append(0)
		elif(word[i] in patt):
			patt.append(word[i])
			ref.append(patt.index(word[i]))
	return ref

def KMP(word, data, IDXlist):
	i = 0
	j = 0
	found = False
	if(len(word)>len(data)):
		print("not found")
		# pass
	else:
		res = 0
		while( found != True) :
			if(j == len(word)):
				# print("found at: "+str(i - j) + "-" + str(i-1))
				
				#Original Code 
				# i = i-j+1
				# j = 0
				#Replacement Code
				j = IDXlist[j-1]
				res +=1

				# found = True
			elif(i == len(data)):
				# print("End of file")
				# found = True
				break
			elif(word[j] == data[i]):
				i+=1
				j+=1
				# print("test")
			elif(word[j] != data[i]):
				# print("test2")
				temp = IDXlist[j-1]
				j = temp
				if(j==0):
					i+=1
				
		if(res == 0):
			print("Not found")
			# pass
		else:
			print(str(res)+" result found")
			# pass	
		# print(j)

def changed_KMP(word, data):
	IDXlist = changed_recurringChar(word)
	print('test')
	i = 0
	j = 0
	found = False
	res = 0
	while( i <= len(data)) :
		if(j == len(word)):
			# print("found at: "+str(i - j) + "-" + str(i-1))
			i = i-j + 1
			j = 0
			# j = IDXlist[j-1]
			res += 1
		elif(i == len(data)):
			# print('henggg')
			break
		elif(word[j] == data[i]):
			i += 1
			j += 1
		elif(word[j] != data[i]):
			if(j == 0):
				i += 1
			
			temp = IDXlist[j]
			j = temp
	# if(res == 0):
	# 	print("not found")
	# else:
	# 	print(str(res)+" result found")
	return res

	# lenW = len(word)
	# lenD = len(data)
	# IDXlist = changed_recurringChar(word)
	# # print('test')
	# i = 0
	# j = 0
	# found = False
	# res = 0
	# while (i <= lenD-1) :
	# 	if(word[j]== data[i]):
	# 		j = j + 1
	# 		i = i + 1
	# 	else:
	# 		if(j != 0):
	# 			temp = IDXlist[j]
	# 			j = temp
	# 		else:
	# 			i = i + 1
	# 	if(j == lenW):
	# 		# print("found at: "+str(i - j) + "-" + str(i-1))
	# 		j = IDXlist[j-1]
	# 		res += 1
	# return res
	

#Boyer Moore
def indexing(word):
	pattern = {}
	wordl = len(word)

	for i in range(wordl) :
		pattern.update({word[i] : max(1, wordl-i-1)})

	# print(pattern)
	return pattern

# Recursive Comparison
def compare(data, word, pattern, pointer_data, pointer_word):
	global result
	# print("Data = " , pointer_data)
	# print("Word = " , pointer_word)
	try:
		if(pointer_data >= len(data)-1):
			return result
		elif data[pointer_data] == word[pointer_word]:
			if pointer_word == 0:
				# print("Found at" , pointer_data , "-", (pointer_data+len(word)-1))
				result += 1
				return compare(data, word, pattern, pointer_data+len(word) , len(word)-1)
			else:
				return compare(data, word, pattern, pointer_data-1, pointer_word-1)

		else:
			if pointer_word == len(data)-1:
				if result == 0:
					# pass
					print("Not Found")
				else:
					# pass
					return result
			else:
				pointer_data += pattern.get(data[pointer_data], len(word)) + (len(word)-1)-pointer_word
				return compare(data, word, pattern, pointer_data, len(word)-1)
	except:
		return False	

def recursiveBoyerMoore(word,data):
	pattern = indexing(word)
	return compare(data, word, pattern, len(word)-1, len(word)-1)

def iterative_compare(data, word, pattern, pointer_data, pointer_word):
	res = 0
	while(pointer_data < (len(data))):
		# print(pointer_data,pointer_word)
		temp_pointer_word = pointer_word
		temp_pointer_data = pointer_data
		while(data[temp_pointer_data] == word[temp_pointer_word]):
			# print(temp_pointer_data,temp_pointer_word)
			if(temp_pointer_word == 0):
				# print("Found at" , temp_pointer_data , "-", (temp_pointer_data+len(word)-1))
				res += 1
				break
			temp_pointer_data -= 1
			temp_pointer_word -= 1
		pointer_data += pattern.get(data[pointer_data], len(word)) + (len(word)-1)-pointer_word
	return res

def iterativeBoyerMoore(word,data):
	pattern = indexing(word)
	# print(pattern)
	return iterative_compare(data, word, pattern, len(word)-1, len(word)-1)
	# return compare(data, word, pattern, len(word)-1, len(word)-1)

def kmp_matcher(t, d):
	n=len(t)
	m=len(d)
	res = 0

	pi = compute_prefix_function(d)
	q = 0
	i = 0
	while i < n:
		if d[q]==t[i]:
			q=q+1
			i = i + 1
		else:
			if q != 0:
				q = pi[q-1]
			else:
				i = i + 1
		if q == m:
			res += 1
			# print ("pattern occurs with shift "+str(i-q))
			q = pi[q-1]
	return res

def compute_prefix_function(p):
	m=len(p)
	pi = [0] * m
	k=1
	l = 0
	while k < m:
		# print(p[k])
		# print(p[l])
		if p[k] <= p[l]:
			l = l + 1
			pi[k] = l
			k = k + 1
		else:
			if l != 0:
				l = pi[l-1]
			else:
				pi[k] = 0
				k = k + 1
	# print(pi)
	return pi

# Word splitting
search = word_input.split(' ')

for v in range(len(search)):
	word = search[v]
	# print("Use KMP Algorithm")
	# start = time()
	# IDXlist = recurringChar(word)
	# # if(max(IDXlist) > 1):
	# KMP(word, data, IDXlist)
	# end = time()
	# print("Took",end - start, "seconds")
	# print()


	# 	if(max(IDXlist) > 1):
	# print("Use KMP Algorithm")
	# start = time()	
	# IDXlist = changed_recurringChar(word)
	# KMP(word, data, IDXlist)
	# end = time()
	# print("Took",end - start, "seconds")
	# print()

	# start = time()
	# # BoyerMoore(word, data)
	# print("Use Recursive Boyer Moore Algorithm")
	# print(recursiveBoyerMoore(word, data), "results found")
	# end = time()
	# print("Took",end - start, "seconds")
	# print()

print("Use changed KMP Algorithm")
start = time()
print(changed_KMP(word, data))
end = time()
print("Took",end - start, "seconds")
print()

# else:
start = time()
# BoyerMoore(word, data)
print("Use Boyer Moore Algorithm")
print(iterativeBoyerMoore(word, data), "results found")
end = time()
print("Took",end - start, "seconds")

	# start = time()
	# print("Use Legit KMP")
	# print(kmp_matcher(data,word))
	# end = time()
	# print("Took",end - start, "seconds")

