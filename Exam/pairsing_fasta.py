# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght 
# Use separate functions for the input and the output 


#a)
f= open('sprot_prot.fasta', 'r')
def line_by_line():
	linebyline= f.readlines()
	return linebyline
#b)
def records(f):
	seq=''
	f= open('sprot_prot.fasta', 'r')
	g= open('records_write.txt','w')
	for line in f:
		if line[0]=='>':
			header=line
		else:
			seq+= line.strip()

		if 'Homo sapiens' not in header:
			k= g.write(header+seq)

	g= open('records_write.txt','r')
	h=g.read().split('\n')[1]
	m=''.join(h)
	d{}
	for i in seq:
		d[i]= m.count(i)
		g= open('records_write.txt','a')
		g.write(d.value(i))



'''
Pseudo-code:
'''
