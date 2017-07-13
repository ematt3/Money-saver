import jinja2

env = None

def init(path):
	global env
	env = jinja2.Environment(loader=jinja2.FileSystemLoader(path))