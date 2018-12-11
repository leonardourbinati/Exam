# average_function.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a function that calculates the average of the values of
# any vector of 10 numbers 
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average 
# Define separate functions for the input and for calculating the average


def input_vector():
	'''This function ask for a 10 variables vector and makes a list of it'''
	vector=list(input("please type a 10 variables' vector: "))
	return vector
print ('input vector= %s' %input_vector())

vector=input_vector()

def average_function(vector):
	'''This function calculates the average of the 10 variables input vector'''
	vector_average= sum(vector)/len(vector)
	return vector_average
print ('input vector average= %s' %(average_function(vector)))
