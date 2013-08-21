
import layout
import networkx
import pyx

accepted_formats = ("pdf", "eps", "ps", "png", "jpg")
pyx.unit.set(xscale = 25)

# from https://github.com/wjrl/BioFabric/blob/master/src/org/systemsbiology/biotapestry/db/ColorGenerator.java
__BIOTAPESTRY_COLORS = (
	pyx.color.hsb(0.0, 1.0, 1.0),
	pyx.color.hsb(0.033, 0.4, 0.9),
	pyx.color.hsb(0.067, 1.0, 1.0),
	pyx.color.hsb(0.1, 1.0, 1.0),
	pyx.color.hsb(0.12, 0.5, 0.8),
	pyx.color.hsb(0.133, 1.0, 1.0),
	pyx.color.hsb(0.183, 0.4, 0.9),
	pyx.color.hsb(0.233, 1.0, 1.0),
	pyx.color.hsb(0.283, 0.5, 0.8),
	pyx.color.hsb(0.333, 1.0, 1.0),
	pyx.color.hsb(0.413, 0.4, 0.9),
	pyx.color.hsb(0.5, 1.0, 1.0),
	pyx.color.hsb(0.534, 0.5, 0.8),
	pyx.color.hsb(0.567, 1.0, 1.0),
	pyx.color.hsb(0.634, 0.35, 0.9),
	pyx.color.hsb(0.667, 1.0, 1.0),
	pyx.color.hsb(0.708, 0.8, 1.0),
	pyx.color.hsb(0.738, 0.5, 0.8),
	pyx.color.hsb(0.767, 1.0, 1.0),
	pyx.color.hsb(0.80, 0.4, 0.9),
	pyx.color.hsb(0.833, 1.0, 1.0),
	pyx.color.hsb(0.917, 0.5, 0.8),
	pyx.color.hsb(0.0, 0.6, 0.55),
	pyx.color.hsb(0.1, 0.5, 0.65),
	pyx.color.hsb(0.12, 1.0, 0.5),
	pyx.color.hsb(0.183, 1.0, 0.5),
	pyx.color.hsb(0.283, 1.0, 0.5),
	pyx.color.hsb(0.534, 1.0, 0.5),
	pyx.color.hsb(0.634, 1.0, 0.5),
	pyx.color.hsb(0.708, 0.6, 0.55),
	pyx.color.hsb(0.80, 1.0, 0.5),
	pyx.color.hsb(0.833, 0.5, 0.65),
)

__palettes = {
	"bw": lambda i: pyx.color.gradient.ReverseGray.getcolor((i % 33) / 40.0),
	"hue": lambda i: pyx.color.gradient.Hue.getcolor((i % 33) / 32.0),
	"rainbow": lambda i: pyx.color.gradient.Rainbow.getcolor((i % 33) / 32.0),
	"default": lambda i: __BIOTAPESTRY_COLORS[i % 32],
}

def draw (graph, filename, format, kwargs):
	(row_to_node, node_to_row), (col_to_edge, edge_to_col), min_col, max_col = layout.process(graph)

	canvas = pyx.canvas.canvas()
	palette = __palettes[kwargs.get("palette", "default")]

	invert = lambda v: len(row_to_node) - v

	# rows
	for i, node in enumerate(row_to_node):
		x1, x2 = min_col[node] * 10, max_col[node] * 10
		y = invert(i) * 10

		canvas.stroke(
			pyx.path.line(x1, y, x2, y),
			[
				pyx.style.linewidth(2),
				palette(i),
				pyx.color.transparency(0.7)
			])

	# columns
	for i, (node_a, node_b) in enumerate(col_to_edge):
		y1 = invert(node_to_row[node_a]) * 10
		y2 = invert(node_to_row[node_b]) * 10
		x = i * 10

		# draw the edge line
		canvas.stroke(
			pyx.path.line(x, y1, x, y2),
			[
				pyx.style.linewidth(2),
				palette(i),
			])

		# draw the end caps
		for y in (y1, y2):
			edge_cap = pyx.path.rect(x - 2.5, y - 2.5, 5, 5)
			canvas.fill(edge_cap, [palette(i)])
			canvas.stroke(edge_cap,	[pyx.style.linewidth(1.75)])

	# node labels
	for i, node in enumerate(row_to_node):
		x1, x2 = min_col[node] * 10, max_col[node] * 10
		y = invert(i) * 10

		label = pyx.text.escapestring(str(node))

		canvas.text(x1 - 5, y + 0.5, label,
			[
				pyx.text.halign.boxright,
				pyx.text.valign.middle
			])

		if (x2 - x1) > 500:
			canvas.text(x2 + 5, y + 0.5, label,
				[
					pyx.text.halign.boxleft,
					pyx.text.valign.middle
				])

	if (format == "pdf"):
		canvas.writePDFfile(filename)
	elif (format == "eps"):
		canvas.writeEPSfile(filename)
	elif (format == "ps"):
		canvas.writePSfile(filename)
	else:
		canvas.writeGSfile(filename, resolution = kwargs.get("resolution", 30))
