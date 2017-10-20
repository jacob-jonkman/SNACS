import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def degree_distribution(G, nodes):
	in_degrees = G.in_degree()
	out_degrees = G.out_degree()
	in_array = np.array([degree[1] for degree in in_degrees])
	out_array = np.array([degree[1] for degree in out_degrees])
	
	# Plot in degrees #
	plt.xlabel("In degree")
	plt.xticks(np.arange(0, 20, 1)) # for medium.in
	#plt.xticks(np.arange(0, 10000, 500)) # for large.in
	plt.ylabel("Frequency")
	plt.yscale('log')
	plt.hist(in_array, bins=20)
	plt.show()
	
	# Plot out degrees #
	plt.xlabel("Out degree")
	plt.ylabel("Frequency")
	plt.xticks(np.arange(0, 400, 25)) # for medium.in
	#plt.xticks(np.arange(0, 10000, 500)) # for large.in
	plt.yscale('log')
	plt.hist(out_array, bins=20)
	plt.show()

def nodes_and_edges(G):
	nodes = G.number_of_nodes()
	edges = G.number_of_edges()
	print("The graph consists of", nodes, "nodes and", edges, "edges.")
	
	return nodes, edges
	
def connected_components(G):
	num_strong = nx.number_strongly_connected_components(G)
	num_weak = nx.number_weakly_connected_components(G)
	
	strong_nodes = [nx.number_of_nodes(Gc) for Gc in nx.strongly_connected_component_subgraphs(G)]
	
	strong_edges = [nx.number_of_edges(Gc) for Gc in nx.strongly_connected_component_subgraphs(G)]

	print("There are a total of", num_strong, "strongly connected components and", num_weak, "weakly connected components.")
	print("The largest strongly connected component consists of", np.max(strong_nodes), "nodes and", np.max(strong_edges), "edges.")
	
	
def compute_distances(G, maxdistance):
	distances = np.zeros(maxdistance, dtype=int)
	for source in nx.nodes(G):
		for target in nx.nodes(G):
			if source != target and nx.has_path(G, source, target):
				distances[nx.shortest_path_length(G, source, target)] += 1
	print(distances)
	
	# Plot distances #
	plt.xlabel("Distance")
	plt.ylabel("Frequency")
	plt.xticks(np.arange(0, maxdistance, 1))
	plt.yscale('log')
	plt.bar(np.arange(maxdistance), distances)
	plt.show()

def main():
	G = nx.read_edgelist("medium.in", create_using=nx.DiGraph())
	#G = nx.read_edgelist("large.in", create_using=nx.DiGraph())
	
	maxdistance = 20 # for medium.in
	#maxdistance = 100 # for large.in
	
	num_nodes, num_edges = nodes_and_edges(G)
	
	degree_distribution(G, num_nodes)
	
	strong, weak = connected_components(G)
	
	compute_distances(G, maxdistance)
	
if __name__ == "__main__":
	main()
