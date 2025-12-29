import sys
libpath = '..\\..\\Extern\\Py2Lib\\lib'
sys.path.append(libpath)

#import utils
import importlib.util
spec = importlib.util.spec_from_file_location('utils', libpath + '/utils.py')
utils = importlib.util.module_from_spec(spec)
sys.modules['utils'] = utils
spec.loader.exec_module(utils)
import cythonizer

pys = utils.findMatchedFiles(".", "*.py")
pys.remove('RootlibCythonizer.py')
moduleLst = cythonizer.run(pys, forceRecompile=True)
moduleNameLst = []
sourceFileLst = []
import os.path
for m in moduleLst:
	for source in m.sources:
		base, ext = os.path.splitext(source)
		moduleName = base.split('/')[-1]
		moduleNameLst.append(moduleName)
		sourceFileLst.append(base + (".cpp" if "c++" == m.language else ".c"))

import sourceWriter

sourceFileName = sourceWriter.run(moduleNameLst, 'rootlib')
print("%s create successful." % sourceFileName)

# not yet implemented.
#from distutils.dist import Distribution

#dist = Distribution({'name' : 'test', 'libraries' : [('test', {'sources' : sourceFileLst})]})

#from builder import Builder
#cBuilder = Builder(dist)
#cBuilder.run()
#import builder
#builder.run(sourceFileLst, 'test')

