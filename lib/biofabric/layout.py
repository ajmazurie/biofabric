# calculate the layout of a biofabric representation of a given graph, based
# on the details of http://www.biomedcentral.com/1471-2105/13/275/

# TODO: implement shadow links
# TODO: implement link groups

import networkx

NEG_INF, POS_INF = float("-inf"), float("+inf")

def _key_with_max_value (d, ignore = None):
	""" find the key with highest value in a dictionary, resolving
		ties by taking the key with highest lexicographic order
	"""
	best_keys, best_value = [], NEG_INF
	if (ignore == None):
		ignore = {}

	for (key, value) in d.iteritems():
		if (key in ignore):
			continue

		if (value > best_value):
			best_keys = [key]
			best_value = value

		elif (value == best_value):
			best_keys.append(key)

	if (len(best_keys) == 0):
		return None, None
	else:
		return sorted(best_keys)[0], best_value

def _order (a, b):
	if (a > b):
		return (b, a)
	else:
		return (a, b)

def process (graph):
	if (not isinstance(graph, networkx.Graph)):
		raise ValueError("invalid object; must be a NetworkX Graph class or subclass")

	if (isinstance(graph, networkx.DiGraph)):
		node_to_neighbors = lambda node: graph.successors(node) + graph.predecessors(node)
	else:
		node_to_neighbors = lambda node: graph.neighbors(node)

	node_to_degree = networkx.degree(graph)

	# phase 1: node assignment
	node_to_row, row_to_node = {}, []
	def node_to_row_ (node):
		if (node in node_to_row):
			return node_to_row[node]
		row_idx = len(node_to_row)
		node_to_row[node] = row_idx
		row_to_node.append(node)
		return row_idx

	while True:
		# find the node with highest degree that has not been assigned a row
		hub, hub_degree = _key_with_max_value(node_to_degree, node_to_row)
		if (hub == None):
			break

		# add it as a new row
		node_to_row_(hub)

		# list its direct neighbors by decreasing degree
		hub_neighbors = reversed(sorted(node_to_neighbors(hub),
			key = lambda node: node_to_degree[node]))

		# add them as new rows, if not assigned already
		for node in hub_neighbors:
			node_to_row_(node)

	assert len(node_to_row) == graph.number_of_nodes() ###

	# phase 2: edge assignment
	edge_to_col, col_to_edge = {}, []
	def edge_to_col_ (edge):
		if (edge in edge_to_col):
			return edge_to_col[edge]
		if (_order(*edge) in edge_to_col):
			return edge_to_col[_order(*edge)]
		edge_idx = len(edge_to_col)
		edge_to_col[edge] = edge_idx
		col_to_edge.append(edge)
		return edge_idx

	min_col, max_col = {}, {}
	for i, node_a in enumerate(row_to_node):
		for node_b in row_to_node[i+1:]:
			if graph.has_edge(node_a, node_b):
				edge_idx = edge_to_col_((node_a, node_b))
				for node in (node_a, node_b):
					min_col[node] = min(min_col.get(node, POS_INF), edge_idx)
					max_col[node] = max(max_col.get(node, NEG_INF), edge_idx)

	assert len(edge_to_col) == graph.number_of_edges() ###

	return (row_to_node, node_to_row), (col_to_edge, edge_to_col), min_col, max_col
