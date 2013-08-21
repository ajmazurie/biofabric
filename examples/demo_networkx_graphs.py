#!/usr/bin/env python

# Display of NetworkX reference graphs using
# biofabric and GraphViz-provided layout

import biofabric
import networkx
import matplotlib.pyplot as plt

generators = (
	(networkx.generators.classic.complete_graph, (10,)),
	(networkx.generators.classic.grid_2d_graph, (5, 5)),
	(networkx.generators.classic.path_graph, (10,)),
	(networkx.generators.classic.ladder_graph, (5,)),
	(networkx.generators.classic.cycle_graph, (10,)),
	(networkx.generators.classic.star_graph, (10,)),
	(networkx.generators.classic.wheel_graph, (10,)),
	(networkx.generators.random_graphs.barabasi_albert_graph, (20, 5)),
	(networkx.generators.social.karate_club_graph, ()),
	(networkx.generators.social.davis_southern_women_graph, ()),
	(networkx.generators.social.florentine_families_graph, ()),
)

for (generator, args) in generators:
	g = generator(*args)

	print "processing '{}' ({:,} nodes, {:,} edges) ...".format(
		generator.__name__, g.number_of_nodes(), g.number_of_edges())

	# draw with biofabric
	biofabric.draw(g, "demo_networkx_graphs/%s-biofabric.png" % generator.__name__)

	# draw with networkx's Matplotlib backend
	plt.figure()
	networkx.draw(g, pos = networkx.graphviz_layout(g, prog = "neato"))
	plt.savefig("demo_networkx_graphs/%s-networkx.png" % generator.__name__)
