# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3
print('exercise_1')
l= range(21,40)
print('l= %s' %l)
for i in l:
	if i%2==0:
		print('even numbers= %s' %i)
	else:
		print('odd numbers= %s' %i)

for i in l:
	if i%3==0:
		print('multiples of 3= %s' %i) 

# Exercise 2
# Print the last two elements of L
print('\nexercise_2')
print('last 2 elements of l= %s' %(l[-2:]))

# Exercise 3
# What's wrong with the following piece of code? Fix it and 
# modify the code in order to have it work AND to have "<i> is in the list" 
# printed at least once
print('\nexercise_3')
L = [1, 2, 3]
print('L= %s' %L)
for i in range(10):
	if i in L:
    		print('i=%s is in the list' %i)
	else:
    		print('i=%s not found' %i)

# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list 
print('\nexercise_4')
f=open('sprot_prot.fasta', 'r')

def first_line_reader(f):
	f=open('sprot_prot.fasta', 'r')
	return(f.readline())
print(first_line_reader(f))

def header(f):
	f=open('sprot_prot.fasta', 'r')
	g= f.readline().split('OS=')[1]
	return g
print header(f)

# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string
print('\nexercise_5')
s= header(f).split()
k= ' '.join(s[0:2])
print k

# Exercise 6
# reverse the string 'asor rosa'
print('\nexercise_6')
string_forward= 'asor rosa'
string_reverse= list(string_forward)[::-1]
string_reverse_2=''.join(string_reverse)
print ('string in reverse= %s' %string_reverse_2)

# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]
print('\nexercise_7')
L= [1, 7, 3, 9]
L= sorted(L)
print('L_sorted= %s' %L)

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L
print('\nexercise_8')
v= sorted(L)
print('new sorted list= %s' %v)

# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6
new_file= open('table.txt','w')
new_file.write('2\t4\n3\t6')
new_file.close()


