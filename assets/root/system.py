import sys
import app
import dbg

sys.path.append("lib")

class TraceFile:
	def write(self, msg):
		dbg.Trace(msg)
	def flush(self):
		pass

class TraceErrorFile:
	def write(self, msg):
		dbg.TraceError(msg)
		dbg.RegisterExceptionString(msg)
	def flush(self):
		pass

class LogBoxFile:
	def __init__(self):
		self.stderrSave = sys.stderr
		self.msg = ""

	def __del__(self):
		self.restore()

	def restore(self):
		sys.stderr = self.stderrSave

	def write(self, msg):
		self.msg = self.msg + msg

	def flush(self):
		pass

	def show(self):
		dbg.LogBox(self.msg,"Error")

sys.stdout = TraceFile()
sys.stderr = TraceErrorFile()

#
# pack file support (must move to system.py, systemrelease.pyc)
#

import marshal
import types
import pack

# Python 3.12 .pyc header is 16 bytes - we just skip it
# No need for magic number constant

class pack_file_iterator(object):
	def __init__(self, packfile):
		self.pack_file = packfile
		
	def __next__(self):
		tmp = self.pack_file.readline()
		if tmp:
			return tmp
		raise StopIteration

_chr = chr

class pack_file(object):

	def __init__(self, filename, mode = 'rb'):
		assert mode in ('r', 'rb')
		if not pack.Exist(filename):
			raise IOError('No file or directory')
		self.data = pack.Get(filename)
		if mode == 'r':
			self.data=_chr(10).join(self.data.split(_chr(13)+_chr(10)))

	def __iter__(self):
		return pack_file_iterator(self)

	def read(self, len = None):
		if not self.data:
			return ''
		if len:
			tmp = self.data[:len]
			self.data = self.data[len:]
			return tmp
		else:
			tmp = self.data
			self.data = ''
			return tmp

	def readline(self):
		return self.read(self.data.find(_chr(10))+1)

	def readlines(self):
		return [x for x in self]

import builtins as _builtins
_builtins.pack_open = pack_open = pack_file

_ModuleType = type(sys)

old_import = __import__
def _process_result(code, fqname):
	# did get_code() return an actual module? (rather than a code object)
	is_module = isinstance(code, _ModuleType)

	# use the returned module, or create a new one to exec code into
	if is_module:
		module = code
	else:
		module = types.ModuleType(fqname)

	# insert additional values into the module (before executing the code)
	#module.__dict__.update(values)

	# the module is almost ready... make it visible
	sys.modules[fqname] = module

	# execute the code within the module's namespace
	if not is_module:
		exec(code, module.__dict__)

	# fetch from sys.modules instead of returning module directly.
	# also make module's __name__ agree with fqname, in case
	# the "exec code in module.__dict__" played games on us.
	module = sys.modules[fqname]
	module.__name__ = fqname
	return module

module_do = lambda x:None

def __pack_import(name, globals=None, locals=None, fromlist=None, level=0):
	if name in sys.modules:
		return sys.modules[name]

	filename = name + '.py'

	if pack.Exist(filename):
		dbg.Trace('importing from pack %s\\n' % name)

		newmodule = _process_result(compile(pack_file(filename,'r').read(),filename,'exec'),name)		

		module_do(newmodule)
		return newmodule
		#return imp.load_module(name, pack_file(filename,'r'),filename,('.py','r',imp.PY_SOURCE))
	else:
		dbg.Trace('importing from lib %s\\n' % name)
		return old_import(name, globals, locals, fromlist, level)

def splitext(p):
	root, ext = '', ''
	for c in p:
		if c in ['/']:
			root, ext = root + ext + c, ''
		elif c == '.':
			if ext:
				root, ext = root + ext, c
			else:
				ext = c
		elif ext:
			ext = ext + c
		else:
			root = root + c
	return root, ext

class PythonExecutioner: 

	def Run(kPESelf, sFileName, kDict): 
		if kPESelf.__IsCompiledFile__(sFileName): 
			kCode=kPESelf.__LoadCompiledFile__(sFileName) 
		else: 
			kCode=kPESelf.__LoadTextFile__(sFileName) 

		exec(kCode, kDict) 

	def __IsCompiledFile__(kPESelf, sFileName): 

		sBase, sExt = splitext(sFileName) 
		sExt=sExt.lower() 

		if sExt==".pyc" or sExt==".pyo": 
			return 1 
		else: 
			return 0 

	def __LoadTextFile__(kPESelf, sFileName): 
		sText=pack_open(sFileName,'r').read() 
		return compile(sText, sFileName, "exec") 

	def __LoadCompiledFile__(kPESelf, sFileName): 
		kFile=pack_open(sFileName)

		# Skip magic number check - just read header
		# Python 3.12 .pyc has 16-byte header: magic(4) + bit field(4) + timestamp(4) + size(4)
		kFile.read(16)

		kData=kFile.read() 
		return marshal.loads(kData) 

def execfile(fileName, dict): 
	kPE=PythonExecutioner() 
	kPE.Run(fileName, dict) 

def exec_add_module_do(mod):
	global execfile
	mod.__dict__['execfile'] = execfile

_builtins.__import__ = __pack_import
module_do = exec_add_module_do

"""
#
# PSYCO installation (must move to system.py, systemrelease.pyc)
#
try:
	import psyco
	#from psyco.classes import *

	def bind_me(bindable_list):
		try:
			for x in bindable_list:
				try:
					psyco.bind(x)
				except Exception:
					pass
		except Exception:
			pass		

	_prev_psyco_old_module_do = module_do
	def module_bind(module):
		_prev_psyco_old_module_do(module)
		#print('start binding' + str(module))
		try:
			psyco.bind(module)
		except Exception:
			pass
		for x in module.__dict__.values():
			try:
				psyco.bind(x)
			except Exception:
				pass		
		#print('end binding')

	dbg.Trace("PSYCO installed\\n")

except Exception as msg:
	bind_me = lambda x:None
	dbg.Trace("No PSYCO support : %s\\n" % msg)
"""

def GetExceptionString(excTitle):
	(excType, excMsg, excTraceBack)=sys.exc_info()
	excText=""
	excText+=_chr(10)

	import traceback
	traceLineList=traceback.extract_tb(excTraceBack)

	for traceLine in traceLineList:
		if traceLine[3]:
			excText+="%s(line:%d) %s - %s" % (traceLine[0], traceLine[1], traceLine[2], traceLine[3])
		else:
			excText+="%s(line:%d) %s"  % (traceLine[0], traceLine[1], traceLine[2])

		excText+=_chr(10)
	
	excText+=_chr(10)
	excText+="%s - %s:%s" % (excTitle, excType, excMsg)		
	excText+=_chr(10)

	return excText

def ShowException(excTitle):
	excText=GetExceptionString(excTitle)
	dbg.TraceError(excText)
	app.Abort()

	return 0

def RunMainScript(name):
	try:		
		execfile(name, __main__.__dict__)
	except RuntimeError as msg:
		msg = str(msg)

		import locale
		if locale.error:
			msg = locale.error.get(msg, msg)

		dbg.LogBox(msg)
		app.Abort()

	except Exception:
		msg = GetExceptionString("Run")
		dbg.LogBox(msg)
		app.Abort()
	
import debugInfo
debugInfo.SetDebugMode(__DEBUG__)

loginMark = "-cs"

RunMainScript("prototype.py")

