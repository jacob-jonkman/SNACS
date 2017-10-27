import networkx as nx
import numpy as np
from time import time
import csv

def to_edgelist(inputfile):
	data = np.genfromtxt(inputfile+".in", dtype=str, delimiter='\n')
	edge_list = [["Source", "Target"]]
	rownumber = 0
	
	for row in data:
		rownumber+=1
		rowArray = row.split('\t')
		user1 = rowArray[1]
		
		# Find the number of mentioned users in this tweet #
		for i in np.arange(row.count('@')):
			index = row.find('@')
			if index > 0:
				j=1
				
				# Look for the first non-number and non-character #
				while index+j+1 < len(row) and row[index+j] != ' ' and row[index+j] != ':' and row[index+j] != '!' and row[index+j] != ')' and row[index+j] != ';' and row[index+j] != '@' and row[index+j] != '"'  and row[index+j] != '.' and row[index+j] != '\xe3':
					j += 1
				
				if(j>1):
					# Parse mentioned username without the @ character #
					user2 = row[index+1:index+j].lower()
					
					if row[index+j] == '.':
						if row[index+j:index+j+4] == ".com" or row[index+j:index+j+4] == ".org" or row[index+j:index+j+4] == ".net" or row[index+j:index+j+3] == ".ir" or row[index+j:index+j+3] == ".ne" or row[index+j:index+j+3] == ".nl" or row[index+j:index+j+3] == ".es" or row[index+j:index+j+4] == ".co." or row[index+j:index+j+3] == ".tv" or row[index+j:index+j+3] == ".de":
							print(user2, row[index-10:min(index+20,len(row))])
							continue
					
					if row[index-1] == ' ' or row[index-1] == '\t' or row[index-1] == '(' or row[index-1] == 'T' or row[index-1] == 't' or row[index-1] == '.' or row[index-1] == ':' or row[index-1]== '!' or row[index-1] == '?' or row[index-1] == '/' or row[index-1] == '-' or row[index-1] == '~' or row[index-1] == ']' or row[index-1] == '[' or row[index-1] == '"':
						#print(user2, row[index-5:min(index+10,len(row))])
						edge_list.append([user1, user2])
					#else:
						#print(user2, row[index-20:min(index+20,len(row))])

				# Continue iterating #
				row = row[index+j:]
	
	print("Sort the edge list")
	edge_list = np.sort(edge_list, 1)
	
	with open(inputfile+'.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(edge_list)
    

def main():
	start_time = time()
	to_edgelist("twitter-small")
	#to_edgelist("twitter-larger")
	print("Program took %s seconds to execute" % (time() - start_time))

if __name__ == "__main__":
	main()
