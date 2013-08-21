
from utils import *
import os, glob

# list available backends
__backends = {}
for fn in glob.glob(os.path.join(os.path.dirname(__file__), "*_backend.py")):
	fn = os.path.basename(fn)
	__backends[fn[:-11]] = fn[:-3]

def draw (graph, filename, format = None, backend = "pyx", **kwargs):
	if (backend in __backends):
		backend_ = __import__(__backends[backend], globals())
	else:
		raise ValueError("unknown backend '%s'" % backend)

	if (format == None):
		if (not '.' in filename):
			raise Exception("unable to infer output format from filename '%s'" % filename)
		format = filename.rsplit('.', 1)[1].lower()

	if (not format in backend_.accepted_formats):
		raise ValueError("backend %s doesn't support %s format" % (backend, format))

	return backend_.draw(graph, filename, format, kwargs)
