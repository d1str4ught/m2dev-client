class Sandbox(object):
	# DO NOT REMOVE ANY ENTRY OF WHITE LIST
	# THIS ENTIES ARE USED FOR Sandbox.
	# 	(If sys.modules['__main__'] is changed, you can see the hell.)
	WHITE_LIST = ['__builtin__', 'types', __name__, '__main__', 'sys']
	def __init__(self, prevent_imported_modules = False, allowed_modules = [], prevented_modules = [], allowed_paths = []):
		self.prevent_imported_modules = prevent_imported_modules
		self.allowed_modules = allowed_modules
		self.prevented_modules = prevented_modules
		self.allowed_paths = allowed_paths
	
	def add_allowed_modules(self, allowed_modules):
		self.allowed_modules = self.allowed_modules + allowed_modules
		
	def add_prevented_modules(self, prevented_modules):
		self.prevented_modules = self.prevented_modules + prevented_modules
	
	def execfile(self, filename, dic):
		import sys
		import copy
				
		for allowed_module_name in self.allowed_modules:
			try:
				exec 'import {0}'.format(allowed_module_name)
			except:
				# Just now, pass the exception.
				# (filename could not use this module)
				sys.stderr.write("Could not import %s" % allowed_module_name)
				pass
		# shallow copy of sys.modules
		old_modules = copy.copy(sys.modules)
		
		old_path = sys.path
		sys.path = self.allowed_paths
	
		# set current imported modules None
		if self.prevent_imported_modules:
			import types
			for k, v in old_modules.items():
				if type(v) == types.ModuleType:
					if not (k in self.WHITE_LIST or k in self.allowed_modules):
						sys.modules[k] = None

		# set prevented modules None.
		for prevented_module_name in self.prevented_modules:
			sys.modules[prevented_module_name] = None
		
		try:
			f = open(filename, 'rb')
			data = f.read()
			code = compile(data, filename, 'exec')
			exec code in dic
		except Exception, e:
			sys.stderr.write(e)
		finally:
			# Restore original settings.
			#sys.modules = old_modules# <- This is not effective. I don't know why, but I guess some where got old sys.modules reference and access old one.
			for k, v in sys.modules.items():
				if not k in old_modules:
					del sys.modules[k]
			for k, v in old_modules.items():
				sys.modules[k] = v
				
			sys.path = old_path


