
import networkx

def graph_from_sif (filename, force_undirected = False):
	""" Import a Cytoscape SIF-formatted graph as a NetworkX directed graph (DiGraph object)

		arguments:
			filename (mandatory) - name of a SIF-formatted file
			force_undirected (optional; default: False) - if True, will return
				an undirected (Graph object) rather than a directed graph (DiGraph object)

		See http://wiki.cytoscape.org/Cytoscape_User_Manual/Network_Formats
	"""
	g = networkx.DiGraph()
	fh = open(filename, "rU")

	while True:
		line = fh.readline()
		if (line == ''):
			break

		line = line.strip()
		if (line == ''):
			continue

		# according to the SIF format documentation, a tab character present in a line
		# means the elements of this line must be separated with a tab, and not spaces
		if ('\t' in line):
			elements = line.split('\t')
		else:
			elements = line.split(' ')

		if (len(elements) != 3):
			raise ValueError("invalid line '%s'" % line)

		node_a, edge_type, node_b = elements
		g.add_edge(node_a, node_b, type = edge_type)

	if (force_undirected):
		return g.to_undirected()
	else:
		return g
