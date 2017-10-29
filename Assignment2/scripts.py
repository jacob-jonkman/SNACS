import networkx as nx
import numpy as np
from time import time
import csv
import re

def to_edgelist(inputfile):
	data = np.genfromtxt(inputfile+".in", dtype=str, delimiter='\n')
	edge_list = [["Source", "Target"]]
	
	# Mentions are from the form @(alphanumeric characters and '_')*(not '.')
	R = re.compile('@[\w_]+[^.]')
	matches = 0
	tweets = len(data)
	
	# Parse the data row for row
	for row in data:
		rowArray = row.split('\t')
		user1 = rowArray[1]
		tweet = rowArray[2]
		
		# Find matches in the tweet according to our regular expression
		M = R.findall(tweet)
		if M:
			matches += len(M)
			for match in M:
				user2 = match[1:]
				
				# Omit last character if needed
				if not user2.isalnum():
					user2 = user2[:-1]
				edge_list.append([user1, user2])
	
	print("%d mentions were found over %d tweets! " %(matches, tweets))
	
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
