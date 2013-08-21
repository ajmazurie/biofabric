biofabric
=========

**biofabric** is a `Python <http://www.python.org/>`_ library implementing the BioFabric network visualization technique described in Longabaugh 2012, *Combing the hairball with BioFabric: a new approach for visualization of large networks* and at http://www.biofabric.org/

BioFabric is a new way to visualize networks in a simple, deterministic way, by laying out nodes and edges as rows and columns on a grid based on their degree. Such visualization allow for the quick identification of hubs, communities, and peculiar network topologies:

.. figure:: http://github.com/ajmazurie/biofabric/raw/master/examples/demo_networkx_graphs/complete_graph-networkx.png
	:align: center
	:width: 700
	:alt: Complete graph (classical representation)

	Complete graph, using a classical representation

.. figure:: http://github.com/ajmazurie/biofabric/raw/master/examples/demo_networkx_graphs/complete_graph-biofabric.png
	:align: center
	:width: 700
	:alt: Complete graph (BioFabric representation)

	Same graph, displayed using the BioFabric technique

Various examples of graphs displayed using BioFabric can be found at http://www.biofabric.org/gallery/index.html and in the ``examples/`` subdirectory.

Getting started
---------------

**biofabric** is provided as an ``easy_install`` and ``pip`` compliant package which can be installed as follows:

- to install the most up to date (and potentially unstable) version, type either ::

	easy_install https://github.com/ajmazurie/biofabric/archive/master.zip
	pip install https://github.com/ajmazurie/biofabric/archive/master.zip

- to install a specific version, such as 0.1.0 (the latest stable version), type either ::

	easy_install https://github.com/ajmazurie/biofabric/archive/0.1.0.zip
	pip install https://github.com/ajmazurie/biofabric/archive/0.1.0.zip

**biofabric** depends on two excellent libraries: `NetworkX <http://networkx.github.io/>`_ to manipulate networks, and `PyX <http://pyx.sourceforge.net/>`_ to produce an output in various formats (pdf, png, eps, jpg, etc.) following the BioFabric technique. ``easy_install`` will install these for you in case they are not already installed in your system.

Once **biofabric** installed, it can be used through the ``draw()`` function::

	import biofabric

	# generate a complete graph of 10 nodes using the
	# networkx library; this is the example shown above
	import networkx
	g = networkx.generators.classic.complete_graph(10)

	# draw it, as a PDF document
	biofabric.draw(g, "complete_graph.pdf")

Documentation and additional examples can be found at https://github.com/ajmazurie/biofabric/wiki

Licensing
---------

**biofabric** is released under a `MIT/X11 license <http://en.wikipedia.org/wiki/MIT_License>`_.
